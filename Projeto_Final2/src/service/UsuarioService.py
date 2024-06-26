from src.model.Usuario import Usuario
from src.repositories.UsuarioRepository import add_usuario

def addUsuario(id: int, Nome: str, Email: str, Senha:str) -> Usuario:
    if(id is None or id == '' or Nome is None or Nome == ''):
        raise Exception
    
    return add_usuario(id, Nome, Email, Senha)