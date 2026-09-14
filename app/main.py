from typing import Optional
from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.models import Machine

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

#Rota Principal com Busca, Filtros e Cards
@app.get("/")
def index(
    request: Request, 
    db: Session = Depends(get_db), 
    q: Optional[str] = None, 
    status: Optional[str] = None
):
    query = db.query(Machine)

    #Filtro de busca por texto (Código, Modelo ou Local)
    if q:
        query = query.filter(
            (Machine.codigo.ilike(f"%{q}%")) | 
            (Machine.modelo.ilike(f"%{q}%")) |
            (Machine.local.ilike(f"%{q}%"))
        )

    #Status
    if status and status != "Todos":
        query = query.filter(Machine.status == status)

    maquinas = query.all()

    #Contador de cards
    total = db.query(Machine).count()
    disponiveis = db.query(Machine).filter(Machine.status == "Disponível").count()
    em_uso = db.query(Machine).filter(Machine.status == "Em uso").count()
    manutencao = db.query(Machine).filter(Machine.status == "Manutenção").count()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "maquinas": maquinas,
            "total": total,
            "disponiveis": disponiveis,
            "em_uso": em_uso,
            "manutencao": manutencao,
            "q": q or "",
            "status_selecionado": status or "Todos"
        }
    )

#Onde Cadastro os novos notebooks
@app.post("/maquinas/criar")
def criar_maquina(
    codigo: str = Form(...),
    modelo: str = Form(...),
    status: str = Form("Disponível"),
    ram: str = Form("-"),
    processador: str = Form("-"),
    placa_video: str = Form("-"),
    armazenamento: str = Form("-"),
    local: str = Form("-"),
    numero_serie: str = Form("-"),
    db: Session = Depends(get_db)
):
    nova_maquina = Machine(
        codigo=codigo,
        modelo=modelo,
        status=status,
        ram=ram,
        processador=processador,
        placa_video=placa_video,
        armazenamento=armazenamento,
        local=local,
        numero_serie=numero_serie
    )
    db.add(nova_maquina)
    db.commit()
    return RedirectResponse(url="/", status_code=303)