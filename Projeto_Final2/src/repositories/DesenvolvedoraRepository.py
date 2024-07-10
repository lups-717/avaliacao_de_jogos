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
    
    desenvolvedora = db.session.query(Desenvolvedora).get(id)
    db.session.delete(desenvolvedora)
    db.session.commit()

def update_desenvolvedora(id: int, nome: str, pais_de_origem: str, especialidade: str) -> Desenvolvedora:
    with db.session.begin():
        desenvolvedora = db.session.query(Desenvolvedora).get(id)
        if desenvolvedora:
             if not nome is None and nome !='':
                desenvolvedora.Nome = nome
             if not pais_de_origem is None and pais_de_origem !='':
                desenvolvedora.Pais_de_origem = pais_de_origem
             if not especialidade is None and especialidade !='':
                desenvolvedora.Especialidade = especialidade



    return desenvolvedora