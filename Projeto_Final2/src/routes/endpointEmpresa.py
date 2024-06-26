from src.controller.EmpresaProprietariaController import EmpresaItem, EmpresaLista

def initialize_endpoints_Empresa(api):
     api.add_resource(EmpresaItem, "/empresas/<int:empresa_id>")
     api.add_resource(EmpresaLista, "/empresas")
