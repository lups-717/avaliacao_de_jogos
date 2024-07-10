from src.controller.UsuarioController import UsuarioItem, UsuarioLista


def initialize_endpoints_Usuario(api):
     api.add_resource(UsuarioItem, "/usuarios/<int:usuario_id>")
     api.add_resource(UsuarioLista, "/usuarios")
