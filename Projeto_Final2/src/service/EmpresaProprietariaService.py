from src.model.EmpresaProprietaria import EmpresaProprietaria
from src.repositories.EmpresaProprietariaRepository import add_EmpresaProprietaria

def addEmpresa(id: int, Nome: str, Descricao: str, Desevolvedora_id:int) -> EmpresaProprietaria:
    if(id is None or id == '' or Nome is None or Nome == ''):
        raise Exception
    
    return add_EmpresaProprietaria(id, Nome, Descricao, Desevolvedora_id)