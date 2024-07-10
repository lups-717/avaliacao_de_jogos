from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .Base import Base

class Avaliacao(Base):
    __tablename__ = "avaliacao"

    id = Column(
        "id",
         Integer,
         primary_key = True,
    )
    Pontuacao = Column("Pontuacao", Float, nullable=False)
    Comentario = Column("Comentario", String(200), nullable=False)
    Jogo_id = Column(Integer, ForeignKey("jogo.id"))
    Usuario_id = Column(Integer, ForeignKey("usuario.id"))

    jogo = relationship("Jogo",back_populates="avaliacao")
    usuario = relationship("Usuario",back_populates="avaliacao")
    def fields(self):
        return {
            "id": self.id,
            "pontuacao": self.Pontuacao,
            "comentario": self.Comentario,
            "jogo_id": self.Jogo_id,
            "usuario_id": self.Usuario_id
        }