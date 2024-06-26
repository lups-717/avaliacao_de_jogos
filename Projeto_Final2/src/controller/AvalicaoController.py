import re
from flask import jsonify, Response
import json
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.repositories.AvaliacaoRepository import get_avaliacaoALL, get_avaliacao, delete_avaliacao, update_avaliacao
from src.service.AvaliacaoService import addAvalicao


class AvaliacaoResponseSchema(Schema):
    id = fields.Int()
    Pontuacao = fields.Float()
    Comentario= fields.Str()
    Jogo_id = fields.Int()
    Usuario_id = fields.Int()

class AvaliacaoRequestSchema(Schema):
    id = fields.Int()
    pontuacao = fields.Float()
    comentario= fields.Str()
    jogo_id = fields.Int()
    usuario_id = fields.Int()
    
    # @validates("Nome")
    # def validate_name(self, value):
    #     if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
    #         raise ValidationError(
    #             "Value must contain only alphanumeric and underscore characters."
    #         )
        
class AvaliacaoItem(MethodResource, Resource):
    @marshal_with(AvaliacaoResponseSchema)
    def get(self, avaliacao_id):
        try:
            avaliacao = get_avaliacao(avaliacao_id)
            if not avaliacao:
                abort(404, message="Resource not found")
            return avaliacao, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, avaliacao_id):
        try:
            delete_avaliacao(avaliacao_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(AvaliacaoRequestSchema, location=("json"))
    @marshal_with(AvaliacaoResponseSchema)
    def put(self, avaliacao_id, **kwargs):
        try:
            avaliacao = update_avaliacao(**kwargs, id=avaliacao_id)
            return avaliacao, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class AvaliacaoLista(MethodResource, Resource):
    @marshal_with(AvaliacaoResponseSchema)
    def get(self):
        try:
            avaliacoes =get_avaliacaoALL()

            print(avaliacoes)
            avaliacao_dicts = [avaliacao.fields() for avaliacao in avaliacoes]
            print(avaliacoes)
            if not avaliacoes:  # Add this line for debugging
                print("No evaluation found")
            json_data = json.dumps(avaliacao_dicts)
            return Response(json_data, 200, mimetype='application/json')
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(AvaliacaoRequestSchema, location=("json"))
    @marshal_with(AvaliacaoResponseSchema)
    def post(self, **kwargs):
        try:
            avaliacao = addAvalicao(**kwargs)
            return avaliacao, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
