from src.model.Jogo import Jogo
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Date
from src.model.Base import db
def add_jogo(id: int, titulo: str, descricao: str, genero: str, data_de_lancamento: Date, empresa_proprietaria_id: int) -> Jogo:
    """
    Insert a funcionario in the database.
    """
    jogo = Jogo(id=id, Titulo=titulo, Descricao = descricao, Genero = genero, Data_de_lancamento = data_de_lancamento, Empresa_Proprietaria_id = empresa_proprietaria_id )
    with db.session.begin():
        db.session.add(jogo)
    return jogo

    return jogo

def get_jogos() -> sqlalchemy.orm.query.Query:
   
    jogo = db.session.query(Jogo).all()
    return jogo

def get_jogo(id: int) -> Jogo:
    """
    Get funcionario by id stored in the database.

    Returns:
        funcionario (Funcionario) -- contains one funcionario registered.
    """
    jogo = db.session.query(Jogo).get(id)
    return jogo

def delete_jogo(id: int):
    """
    Delete funcionario by id stored in the database.

    """
    jogo = db.session.query(Jogo).get(id)
    db.session.delete(jogo)
    db.session.commit()

def update_jogo(id: int, titulo: str, descricao: str, genero: str, data_de_lancamento:Date, empresa_proprietaria_id:int) -> Jogo:
    """
    Insert a Funcionario in the database.
    """
    jogo = db.session.query(Jogo).get(id)
    
    jogo.Titulo = titulo
    jogo.Descricao = descricao
    jogo.Genero = genero
    jogo.Data_de_lancamento = data_de_lancamento
    jogo.Empresa_Proprietaria_id = empresa_proprietaria_id

    db.session.commit()

    return jogo