from sqlalchemy.types import Date
from datetime import datetime,date
from src.model.Jogo import Jogo
from src.repositories.JogoRepository import add_jogo

data_referencia = date(1967, 1, 1)


def addJogo(id: int, titulo: str, descricao: str, genero:str, data_de_lancamento: Date, empresa_proprietaria_id: int) -> Jogo:

    if(id is None or id == '' or titulo is None or titulo == ''):
        raise Exception
    if isinstance(data_de_lancamento, str):
        data = datetime.strptime(data_de_lancamento, '%Y-%m-%d').date()
    else:
        data = data_de_lancamento
    if(data < data_referencia):
        raise Exception
    return add_jogo(id, titulo, descricao, genero, data_de_lancamento, empresa_proprietaria_id)