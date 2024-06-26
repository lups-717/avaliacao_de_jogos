from src.model.EmpresaProprietaria import EmpresaProprietaria
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_EmpresaProprietaria(id: int, Nome: str, Descricao: str, Desenvolvedora_id: int) -> EmpresaProprietaria:
    empresa = EmpresaProprietaria(id=id, Nome=Nome, Descricao=Descricao, Desenvolvedora_id=Desenvolvedora_id)
    with db.session.begin():
        db.session.add(empresa)
    return empresa

def get_empresas() -> sqlalchemy.orm.query.Query:
    """
    Get all funcionarios stored in the database.

    Returns:
        funcionarios (Funcionario) -- contains all funcionarios registered.
    """
    empresa = db.session.query(EmpresaProprietaria).all()
    return empresa

def get_empresa(id: int) -> add_EmpresaProprietaria:
    """
    Get funcionario by id stored in the database.

    Returns:
        funcionario (Funcionario) -- contains one funcionario registered.
    """
    empresa = db.session.query(EmpresaProprietaria).get(id)
    return empresa

def delete_empresa(id: int):
    """
    Delete funcionario by id stored in the database.

    """
    empresa = db.session.query(EmpresaProprietaria).get(id)
    db.session.delete(empresa)
    db.session.commit()

def update_empresa(id: int, Nome: str, Descricao: str, Desenvolvedora_id: int) -> EmpresaProprietaria:
    """
    Insert a Funcionario in the database.
    """
    empresa = db.session.query(EmpresaProprietaria).get(id)
    
    empresa.Nome = Nome
    empresa.Pais_de_origem = Descricao
    empresa.Especialidade = Desenvolvedora_id

    db.session.commit()

    return empresa