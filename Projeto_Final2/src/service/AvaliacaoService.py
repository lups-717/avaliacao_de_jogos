from src.model.Avaliacao import Avaliacao
from src.repositories.AvaliacaoRepository import add_avaliacao

def addAvalicao(id: int, Pontuacao: float, Comentario: str, jogo_id: int, Usuario_id:int) -> Avaliacao:
    if(id is None or id == '' or Pontuacao is None or Pontuacao > 10 or Pontuacao < 0):
        raise Exception
    
    return add_avaliacao(id,  Pontuacao , Comentario, jogo_id, Usuario_id)