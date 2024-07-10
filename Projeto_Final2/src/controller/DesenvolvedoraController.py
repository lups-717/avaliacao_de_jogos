import re
from flask import jsonify, Response
import json
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.repositories.DesenvolvedoraRepository import get_desenvolvedoras, get_desenvolvedora, delete_desenvolvedora, update_desenvolvedora
from src.service.DesenvolvedoraService import addDesenvolvedora


class DesenvolvedoraResponseSchema(Schema):
    id = fields.Int()
    Nome = fields.Str()
    Pais_de_origem = fields.Str()
    Especialidade = fields.Str()

class DesenvolvedoraRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    pais_de_origem = fields.Str()
    especialidade = fields.Str()
    
    # @validates("nome")
    # def validate_name(self, value):
    #     if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
    #          raise ValidationError(
    #              "Value must contain only alphanumeric and underscore characters."
    #         )
        
class DesenvolvedoraItem(MethodResource, Resource):
    @marshal_with(DesenvolvedoraResponseSchema)
    def get(self, desenvolvedora_id):
        try:
            desenvolvedora = get_desenvolvedora(desenvolvedora_id)
            if not desenvolvedora:
                abort(404, message="Resource not found")
            return desenvolvedora, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, desenvolvedora_id):
        try:
            delete_desenvolvedora(desenvolvedora_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(DesenvolvedoraRequestSchema, location=("json"))
    @marshal_with(DesenvolvedoraResponseSchema)
    def put(self, desenvolvedora_id, **kwargs):
        try:
            kwargs['id'] = desenvolvedora_id
            desenvolvedora = update_desenvolvedora(**kwargs)
            return desenvolvedora, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")


class DesenvolvedoraLista(MethodResource, Resource):
    @marshal_with(DesenvolvedoraResponseSchema)
    def get(self):
        try:
            desenvolvedoras = get_desenvolvedoras()
            desenvolvedora_dicts = [desenvolvedora.fields() for desenvolvedora in desenvolvedoras]
            print(f"User dicts: {desenvolvedora_dicts}")
            if not desenvolvedoras:  # Add this line for debugging
                print("No users found")
            json_data = json.dumps(desenvolvedora_dicts)
            return Response(json_data, 200, mimetype='application/json')
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(DesenvolvedoraRequestSchema, location=("json"))
    @marshal_with(DesenvolvedoraResponseSchema)
    def post(self, **kwargs):
        try:
            desenvolvedora = addDesenvolvedora(**kwargs)
            return desenvolvedora, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
