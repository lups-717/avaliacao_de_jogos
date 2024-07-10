from src.model.Avaliacao import Avaliacao
from src.repositories.AvaliacaoRepository import add_avaliacao

def addAvalicao(id: int, pontuacao: float, comentario: str, jogo_id: int, usuario_id:int) -> Avaliacao:
    if(id is None or id == '' ):
        raise Exception
    if pontuacao is None or pontuacao > 10 or pontuacao < 0:
        raise Exception
    return add_avaliacao(id,  pontuacao , comentario, jogo_id, usuario_id)