import re
from flask import jsonify, Response
import json
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.repositories.EmpresaProprietariaRepository import get_empresas, get_empresa, delete_empresa, update_empresa
from src.service.EmpresaProprietariaService import addEmpresa



class EmpresaResponseSchema(Schema):
    id = fields.Int()
    Nome = fields.Str()
    Descricao = fields.Str()
    Densenvolvedora_id =  fields.Int()

class EmpresaRequestSchema(Schema):
    id = fields.Int()
    Nome = fields.Str()
    Descricao = fields.Str()
    Densenvolvedora_id =  fields.Int()

    
    @validates("Nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
class EmpresaItem(MethodResource, Resource):
    @marshal_with(EmpresaResponseSchema)
    def get(self, empresa_id):
        try:
            empresa = get_empresa(empresa_id)
            if not empresa:
                abort(404, message="Resource not found")
            return empresa, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, empresa_id):
        try:
            delete_empresa(empresa_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(EmpresaRequestSchema, location=("form"))
    @marshal_with(EmpresaResponseSchema)
    def put(self, empresa_id, **kwargs):
        try:
            empresa = update_empresa(**kwargs, id=empresa_id)
            return empresa, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

class EmpresaLista(MethodResource, Resource):
    @marshal_with(EmpresaResponseSchema)
    def get(self):
        try:
            empresas = get_empresas()
            empresa_dicts = [empresa.fields() for empresa in empresas]
            print(f"User dicts: {empresa_dicts}")
            if not empresas:  # Add this line for debugging
                print("No users found")
            json_data = json.dumps(empresa_dicts)
            return Response(json_data, 200, mimetype='application/json')
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(EmpresaResponseSchema, location=("form"))
    @marshal_with(EmpresaResponseSchema)
    def post(self, **kwargs):
        try:
            empresa = addEmpresa(**kwargs)
            return empresa, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
