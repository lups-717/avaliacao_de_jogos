import re
from flask import jsonify, Response
import json
from flask_restful import Resource, abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.repositories.UsuarioRepository import get_usuarios, get_usuario, delete_usuario, update_usuario
from src.service.UsuarioService import addUsuario


# Esquema de resposta do usuário
class UsuarioResponseSchema(Schema):
    id = fields.Int()
    Nome = fields.Str()
    Email = fields.Str()
    Senha = fields.Str()

# Esquema de solicitação do usuário
class UsuarioRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str(required=True)
    email = fields.Str(required=True)
    senha = fields.Str(required=True)

    # @validates("Email")
    # def validate_email(self, value):
    #     if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
    #         raise ValidationError("Value must contain only alphanumeric and underscore characters.")

# Recurso de item do usuário
class UsuarioItem(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema)
    def get(self, usuario_id):
        try:
            usuario = get_usuario(usuario_id)
            if not usuario:
                abort(404, message="Resource not found")
            return usuario, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, usuario_id):
        try:
            delete_usuario(usuario_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Resource not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

    @use_kwargs(UsuarioRequestSchema, location="json")
    @marshal_with(UsuarioResponseSchema)
    def put(self, usuario_id, **kwargs):
        try:
            kwargs['id'] = usuario_id
            usuario = update_usuario(**kwargs)
            return usuario, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Internal Server Error")

# Recurso da lista de usuários
class UsuarioLista(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema)
    def get(self):
        try:
            users = get_usuarios()
            print(f"Users: {users}")
            user_dicts = [user.fields() for user in users]
            print(f"User dicts: {user_dicts}")
            if not users:  # Add this line for debugging
                print("No users found")
            json_data = json.dumps(user_dicts)
            return Response(json_data, 200, mimetype='application/json')
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(UsuarioRequestSchema, location="json")
    @marshal_with(UsuarioResponseSchema)
    def post(self, **kwargs):
            try:
                usuario = addUsuario(**kwargs)
                return usuario, 201
            except IntegrityError as err:
                abort(500, message=str(err.__context__))
            except OperationalError as err:
                abort(500, message=str(err.__context__))


'''
class UsuarioLista(MethodResource, Resource):
    @marshal_with(UsuarioResponseSchema)
    def get():
        try:
            return get_usuarios(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")
'''