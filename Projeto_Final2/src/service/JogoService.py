from src.model.Jogo import Jogo
from src.repositories.JogoRepository import add_jogo

def addJogo(id: int, Título: str, Descricao: str, Genero:str,Data_lancamento ) -> Jogo:
    if(id is None or id == '' or Título is None or Título == ''):
        raise Exception
    
    return add_jogo(id, Título, Descricao, Genero, Data_lancamento)