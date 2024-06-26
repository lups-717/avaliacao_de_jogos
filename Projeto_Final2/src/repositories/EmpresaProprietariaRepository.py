from src.model.EmpresaProprietaria import EmpresaProprietaria
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Base import db

def add_EmpresaProprietaria(id: int, nome: str, descricao: str, desenvolvedora_id: int) -> EmpresaProprietaria:
    empresa = EmpresaProprietaria(id=id, Nome=nome, Descricao=descricao, Desenvolvedora_id=desenvolvedora_id)
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

def update_empresa(id: int, nome: str, descricao: str, desenvolvedora_id: int) -> EmpresaProprietaria:
    """
    Insert a Funcionario in the database.
    """
    empresa = db.session.query(EmpresaProprietaria).get(id)
    
    empresa.Nome = nome
    empresa.Pais_de_origem = descricao
    empresa.Especialidade = desenvolvedora_id

    db.session.commit()

    return empresa