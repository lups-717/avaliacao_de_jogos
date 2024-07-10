from flask import Flask
from flask_restful import Api
from src.routes.endpointEmpresa import initialize_endpoints_Empresa
from src.routes.endpointAvalicao import initialize_endpoints_Avaliacao
from src.routes.endpointJogo import initialize_endpoints_Jogo
from src.routes.endpointUsuario import initialize_endpoints_Usuario
from src.routes.endpointDesenvolvedora import initialize_endpoints_Desenvolvedora
from src.model.Base import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/gamesreview'
    db.init_app(app)

    # Flask API
    api = Api(app, prefix="/api")
    initialize_endpoints_Desenvolvedora(api)
    initialize_endpoints_Jogo(api)
    initialize_endpoints_Avaliacao(api)
    initialize_endpoints_Empresa(api)
    initialize_endpoints_Usuario(api)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
