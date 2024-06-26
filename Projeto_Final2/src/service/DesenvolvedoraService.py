from src.model.Desenvolvedora import Desenvolvedora
from src.repositories.DesenvolvedoraRepository import add_Desenvolvedora 

def addDesenvolvedora(id: int, Nome: str, Descricao: str, Desevolvedora_id:int) -> Desenvolvedora:
    if(id is None or id == '' or Nome is None or Nome == ''):
        raise Exception
    
    return add_Desenvolvedora(id, Nome, Descricao, Desevolvedora_id)