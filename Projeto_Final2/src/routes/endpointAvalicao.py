from src.controller.AvalicaoController import AvaliacaoItem, AvaliacaoLista

def initialize_endpoints_Avaliacao(api):
    api.add_resource(AvaliacaoItem, "/avaliacoes/<int:avalicao_id>")
    api.add_resource(AvaliacaoLista, "/avaliacoes")
