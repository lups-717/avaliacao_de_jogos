from src.model.Avaliacao import Avaliacao
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Date
from src.model.Base import db

def add_avaliacao(id: int, pontuacao: float , comentario: str, jogo_id: int, usuario_id:int) -> Avaliacao:
    avaliacao = Avaliacao(id=id, Pontuacao= pontuacao, Comentario = comentario, Jogo_id = jogo_id, Usuario_id = usuario_id)
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

def update_avaliacao(id: int, pontuacao: str, comentario: str, jogo_id: int, usuario_id:int) -> Avaliacao:
    """
    Insert a Funcionario in the database.
    """
    avaliacao = db.session.query(Avaliacao).get(id)
    
    avaliacao.Pontuacao = pontuacao
    avaliacao.Comentario = comentario
    avaliacao.jogo_id = jogo_id
    avaliacao.Usuario_id = usuario_id

    db.session.commit()

    return avaliacao