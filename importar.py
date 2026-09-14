import pandas as pd
from app.database import SessionLocal, engine, Base
from app.models import Machine

Base.metadata.create_all(bind=engine)

db = SessionLocal()

excel_file = r"C:\Users\luisf\Downloads\Estoque do notebook.xlsx"
df = pd.read_excel(excel_file, sheet_name=0)

df.columns = df.columns.str.strip()

print(f"Lendo {len(df)} registros da planilha...")

for _, row in df.iterrows():
    notebook = Machine(
        codigo=str(row["CODIGO DA MAQUINA"]),
        modelo=str(row["MODELO"]) if pd.notna(row["MODELO"]) else "-",
        status=str(row["STATUS"]) if pd.notna(row["STATUS"]) else "Disponível",
        ram=str(row["RAM"]) if pd.notna(row["RAM"]) else "-",
        processador=str(row["PROCESSADOR"]) if pd.notna(row["PROCESSADOR"]) else "-", 
        placa_video=str(row["PLACA DE VIDEO"]) if pd.notna(row["PLACA DE VIDEO"]) else "-",
        armazenamento=str(row["ARMAZENAMENTO"]) if pd.notna(row["ARMAZENAMENTO"]) else "-",
        local=str(row["LOCAL"]) if pd.notna(row["LOCAL"]) else "-",
        numero_serie=str(row["NUMERO DE SERIE"]) if pd.notna(row["NUMERO DE SERIE"]) else "-"
    )
    db.add(notebook)
db.commit()
db.close()
print("✅ Sucesso! Todos os notebooks foram cadastrados no PostgreSQL.")