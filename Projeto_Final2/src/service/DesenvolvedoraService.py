from src.model.Desenvolvedora import Desenvolvedora
from src.repositories.DesenvolvedoraRepository import add_Desenvolvedora 
        
def addDesenvolvedora(id: int, nome: str, pais_de_origem: str, especialidade:str) -> Desenvolvedora:
    if(id is None or id == '' or nome is None or nome == ''):
        raise Exception
    if not pais_de_origem[0].isupper():
        raise ValueError("A string deve começar com uma letra maiúscula.")
    if any(char.isdigit() for char in pais_de_origem):
        raise ValueError("A string não deve conter números.")
    if any(not char.isalnum() for char in especialidade):
        raise ValueError("A string não deve conter caracteres especiais.")
    return add_Desenvolvedora(id, nome, pais_de_origem, especialidade)