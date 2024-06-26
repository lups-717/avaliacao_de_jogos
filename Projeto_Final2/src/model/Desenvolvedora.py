from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import Base


class Desenvolvedora(Base):
    __tablename__ = "desenvolvedora"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    Nome = Column("Nome", String(150), nullable=False)
    Pais_de_origem = Column("Pais_de_origem", String(45), nullable=False)
    Especialidade = Column("Especialidade", String(45), nullable=False)
    
    empresa = relationship("EmpresaProprietaria",back_populates="desenvolvedora")
    def fields(self):
        return {
            "id": self.id,
            "nome": self.Nome,
            "pais de origem": self.Pais_de_origem,
            "Especialidade": self.Especialidade
        }