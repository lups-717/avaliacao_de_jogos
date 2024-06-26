from src.model.Avaliacao import Avaliacao
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Date
from src.model.Base import db

def add_avaliacao(id: int, Pontuacao: float , Comentario: str, jogo_id: int, Usuario_id:int) -> Avaliacao:
    avaliacao = Avaliacao(id=id, Pontuacao= Pontuacao, Comentario = Comentario,jogo_id =jogo_id,Usuario_id = Usuario_id)
    with db.session.begin():
        db.session.add(avaliacao)
    return avaliacao

def get_avaliacaoALL() -> sqlalchemy.orm.query.Query:
   
    return db.session.query(Avaliacao).all()
     

def get_avaliacao(id: int) -> Avaliacao:
    """
    Get funcionario by id stored in the database.

    Returns:
        funcionario (Funcionario) -- contains one funcionario registered.
    """
    avaliacao = db.session.query(Avaliacao).get(id)
    return avaliacao

def delete_avaliacao(id: int):
    """
    Delete funcionario by id stored in the database.

    """
    avaliacao = db.session.query(Avaliacao).get(id)
    db.session.delete(avaliacao)
    db.session.commit()

def update_avaliacao(id: int, Pontuacao: str, Comentario: str, jogo_id: int, Usuario_id:int) -> Avaliacao:
    """
    Insert a Funcionario in the database.
    """
    avaliacao = db.session.query(Avaliacao).get(id)
    
    avaliacao.Pontuacao = Pontuacao
    avaliacao.Comentario = Comentario
    avaliacao.jogo_id = jogo_id
    avaliacao.Usuario_id = Usuario_id

    db.session.commit()

    return avaliacao