from pymongo import MongoClient
from marshmallow import fields, Schema
import os


class Conexao:
    def __init__(self):
        self.ambiente = os.getenv("AMBIENTE")
        self.porta = os.getenv("PORTA_BANCO")
        self.banco = os.getenv("BANCO")
        self.nome_collection = os.getenv("COLLECTION_PACIENTES")

    def process(self):
        cliente = MongoClient("localhost", 17017)
        banco = cliente["tcc"]
        pacientes = banco["usuarios"]

        return pacientes


class UsuarioSchema(Schema):
    _id = fields.Str()
    usuario = fields.Str()
    senha = fields.Str()
    email = fields.Str()
    perfil = fields.Str()
