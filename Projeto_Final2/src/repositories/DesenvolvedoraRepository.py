from src.model.Desenvolvedora import Desenvolvedora
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db
def add_Desenvolvedora(id: int, nome: str, pais_de_origem: str, especialidade: str) -> Desenvolvedora:
    print(nome)
    desenvolvedora = Desenvolvedora(id=id, Nome = nome, Pais_de_origem = pais_de_origem, Especialidade = especialidade)
    with db.session.begin():
        db.session.add(desenvolvedora)
    return desenvolvedora

def get_desenvolvedoras() -> sqlalchemy.orm.query.Query:
    
    return  db.session.query(Desenvolvedora).all()
     

def get_desenvolvedora(id: int) -> Desenvolvedora:
    """
    Get funcionario by id stored in the database.

    Returns:
        funcionario (Funcionario) -- contains one funcionario registered.
    """
    return db.session.query(Desenvolvedora).get(id)
     

def delete_desenvolvedora(id: int):
    """
    Delete funcionario by id stored in the database.

    """
    desenvolvedora = db.session.query(Desenvolvedora).get(id)
    db.session.delete(desenvolvedora)
    db.session.commit()

def update_desenvolvedora(id: int, nome: str, pais_de_origem: str, especialidade: str) -> Desenvolvedora:
    """
    Insert a Funcionario in the database.
    """
    desenvolvedora = db.session.query(Desenvolvedora).get(id)
    
    desenvolvedora.Nome = nome
    desenvolvedora.Pais_de_origem = pais_de_origem
    desenvolvedora.Especialidade = especialidade

    db.session.commit()

    return desenvolvedora