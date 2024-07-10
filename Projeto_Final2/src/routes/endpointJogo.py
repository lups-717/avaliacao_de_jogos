from src.controller.JogoController import JogoItem, JogoLista

def initialize_endpoints_Jogo(api):
     api.add_resource(JogoItem, "/jogos/<int:jogo_id>")
     api.add_resource(JogoLista, "/jogos")
