from sqlalchemy.types import Date
from src.model.Jogo import Jogo
from src.repositories.JogoRepository import add_jogo

def addJogo(id: int, titulo: str, descricao: str, genero:str, data_de_lancamento: Date, empresa_proprietaria_id: int) -> Jogo:
    if(id is None or id == '' or titulo is None or titulo == ''):
        raise Exception
    
    return add_jogo(id, titulo, descricao, genero, data_de_lancamento, empresa_proprietaria_id)