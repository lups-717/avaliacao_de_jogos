from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from .Base import Base

class Jogo(Base):
    __tablename__ = "jogo"

    id = Column(
        "id",
         Integer,
         primary_key = True,
    )
    Titulo = Column("Titulo", String(150), nullable=False)
    Descricao = Column("Descricao", String(200), nullable=False)
    Genero = Column("Genero", String(45), nullable=False)
    Data_de_lancamento = Column("Data_de_lancamento", Date , nullable=False)

    Empresa_Proprietaria_id = Column(Integer, ForeignKey("empresa_proprietaria.id"), nullable=False)
    # Empresa_Proprietaria_Desenvolvedora_id = Column(Integer, ForeignKey("desenvolvedora.id"), nullable=False)


    empresa = relationship("EmpresaProprietaria",back_populates="jogo")
    avaliacao = relationship("Avaliacao",back_populates="jogo")
    def fields(self):
        return {
            "id": self.id,
            "titulo": self.Titulo,
            "descricao":self.Descricao,
            "genero": self.Genero,
            "data_de_lancamento": self.Data_de_lancamento.strftime('%Y-%m-%d'),
            "empresa_proprietaria_id": self.Empresa_Proprietaria_id
        }