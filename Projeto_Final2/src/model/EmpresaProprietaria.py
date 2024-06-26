from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#from sqlalchemy import SQLAlchemy
from .Base import Base
#db = SQLAlchemy()
class EmpresaProprietaria(Base):
    __tablename__= "empresa_proprietaria"

    id = Column(
        "id",
         Integer,
         primary_key = True,
    )
    Nome = Column("Nome",String(45),nullable=False)
    Descricao = Column("Descricao", String(150), nullable=False )

    Desenvolvedora_id = Column(Integer, ForeignKey("desenvolvedora.id"), nullable=False)
    
   # jogo = relationship("Jogo",backref=db.backref("empresa", lazy = True))
    jogo = relationship("Jogo",back_populates="empresa")
    desenvolvedora = relationship("Desenvolvedora",back_populates="empresa")
    
    #falta auto encremento no id sinalizar isso aqui no modelo
    def fields(self):
        return {
            "id": self.id,
            "nome": self.Nome,
            "Descricao": self.Descricao,
            "desenvolvedora_id": self.Desenvolvedora_id
        }