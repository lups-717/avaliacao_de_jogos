from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
##from src.model.Base import Base
from src.model.Base import Base


class Usuario(Base):
    __tablename__ = "usuario"

    # Columns
    id = Column(
        "id",
        Integer,
        primary_key=True,
    )
    Nome = Column("Nome", String(150), nullable=False)
    Email = Column("Email", String(150), nullable=False)
    Senha = Column("Senha", String(150), nullable=False)
    
    avaliacao = relationship("Avaliacao",back_populates="usuario")
    def fields(self):
        return {
            "id": self.id,
            "nome": self.Nome,
            "email": self.Email,
            "senha": self.Senha
        }