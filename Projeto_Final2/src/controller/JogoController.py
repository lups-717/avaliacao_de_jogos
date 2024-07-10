import re
from flask import jsonify, Response
import json
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.repositories.JogoRepository import get_jogos, get_jogo, delete_jogo, update_jogo
from src.service.JogoService import addJogo


class JogoResponseSchema(Schema):
    id = fields.Int()
    Titulo = fields.Str()
    Descricao = fields.Str()
    Genero =  fields.Str()
    Data_de_lancamento =fields.Date()
    Empresa_Proprietaria_id = fields.Int()
class JogoRequestSchema(Schema):
    id = fields.Int()
    titulo = fields.Str()
    descricao = fields.Str()
    genero =  fields.Str()
    data_de_lancamento =fields.Date()
    empresa_proprietaria_id = fields.Int()

    
class JogoItem(MethodResource, Resource):
    @marshal_with(JogoResponseSchema)
    def get(self, jogo_id):
        try:
            jogo = get_jogo(jogo_id)
            if not jogo:
                abort(404, message="Resource not found")
            return jogo, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, jogo_id):
        try:
            delete_jogo(jogo_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(JogoRequestSchema, location=("json"))
    @marshal_with(JogoResponseSchema)
    def put(self, jogo_id, **kwargs):
        try:
            kwargs['id'] = jogo_id
            jogo = update_jogo(**kwargs)
            return jogo, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

class JogoLista(MethodResource, Resource):
    @marshal_with(JogoResponseSchema)
    def get(self):
        try:
            jogos = get_jogos()
            jogo_dicts = [jogo.fields() for jogo in jogos]
            if not jogos:  # Add this line for debugging
                print("No users found")
            json_data = json.dumps(jogo_dicts)
            return Response(json_data, 200, mimetype='application/json')
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(JogoRequestSchema, location=("json"))
    @marshal_with(JogoResponseSchema)
    def post(self, **kwargs):
        try:
            jogo = addJogo(**kwargs)
            return jogo, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
