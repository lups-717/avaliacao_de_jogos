from flask import Flask
from flask_restful import Api
from src.routes.endpointEmpresa import initialize_endpoints_Empresa
from src.routes.endpointAvalicao import initialize_endpoints_Avaliacao
from src.routes.endpointJogo import initialize_endpoints_Jogo
from src.routes.endpointUsuario import initialize_endpoints_Usuario
from src.routes.endpointDesenvolvedora import initialize_endpoints_Desenvolvedora
from src.model.Base import db
from app import create_app

app = create_app()
