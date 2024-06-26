from src.model.EmpresaProprietaria import EmpresaProprietaria
from src.repositories.EmpresaProprietariaRepository import add_EmpresaProprietaria

def addEmpresa(id: int, nome: str, descricao: str, desenvolvedora_id:int) -> EmpresaProprietaria:
    if(id is None or id == '' or nome is None or nome == ''):
        raise Exception
    
    return add_EmpresaProprietaria(id, nome, descricao, desenvolvedora_id)