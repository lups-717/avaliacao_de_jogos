from src.controller.DesenvolvedoraController import DesenvolvedoraItem, DesenvolvedoraLista

def initialize_endpoints_Desenvolvedora(api):
     api.add_resource(DesenvolvedoraItem, "/desenvolvedoras/<int:Desenvolvedora_id>")
     api.add_resource(DesenvolvedoraLista, "/desenvolvedoras")
