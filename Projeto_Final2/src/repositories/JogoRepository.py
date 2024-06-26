from src.model.Jogo import Jogo
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Date
from src.model.Base import db
def add_jogo(id: int, Titulo: str, Descricao: str, Genero: str, Data_de_lancamento:Date,Empresa_Proprietaria_id:int, Empresa_Proprietária_Desenvolvedora_id) -> Jogo:
    """
    Insert a funcionario in the database.
    """
    jogo = Jogo(id=id, Titulo=Titulo, Descricao = Descricao, Genero = Genero, Data_de_lancamento = Data_de_lancamento, Empresa_Proprietaria_id = Empresa_Proprietaria_id )
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

def update_jogo(id: int, Titulo: str, Descricao: str, Genero: str, Data_de_lancamento:Date, Empresa_Proprietaria_id:int, Empresa_Proprietária_Desenvolvedora_id) -> Jogo:
    """
    Insert a Funcionario in the database.
    """
    jogo = db.session.query(Jogo).get(id)
    
    jogo.Titulo = Titulo
    jogo.Descricao = Descricao
    jogo.Genero = Genero
    jogo.Data_de_lancamento = Data_de_lancamento
    jogo.Empresa_Proprietaria_id = Empresa_Proprietaria_id
    jogo.Empresa_Proprietária_Desenvolvedora_id = Empresa_Proprietária_Desenvolvedora_id

    db.session.commit()

    return jogo