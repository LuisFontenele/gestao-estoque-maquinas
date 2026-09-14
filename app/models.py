from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, index=True)
    modelo = Column(String)
    status = Column(String, default="Disponível")
    ram = Column(String)
    processador = Column(String)
    placa_video = Column(String)
    armazenamento = Column(String)
    local = Column(String)
    numero_serie = Column(String)
