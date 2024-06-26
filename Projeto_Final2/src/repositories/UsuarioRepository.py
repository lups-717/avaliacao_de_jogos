import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from src.model.Usuario import Usuario
from src.model.Base import db


def add_usuario(id: int, nome: str, email: str, senha: str) -> Usuario:
    """Insert a usuario in the database."""
    usuario = Usuario(id=id, nome=nome, email=email, senha=senha)
    with db.session.begin():
        db.session.add(usuario)
    return usuario

def get_usuarios() -> sqlalchemy.orm.query.Query:
    """Get all usuarios stored in the database."""
    return db.session.query(Usuario).all()

def get_usuario(id: int) -> Usuario:
    """Get usuario by id stored in the database."""
    return db.session.query(Usuario).get(id)

def delete_usuario(id: int) -> None:
    """Delete usuario by id stored in the database."""
    with db.session.begin():
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            db.session.delete(usuario)

def update_usuario(id: int, nome: str, email: str, senha: str) -> Usuario:
    """Update a usuario in the database."""
    with db.session.begin():
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
    return usuario