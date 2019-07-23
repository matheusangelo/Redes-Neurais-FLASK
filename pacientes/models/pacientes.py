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
        print(os.getenv("AMBIENTE"))
        cliente = MongoClient(self.ambiente,17017)
        banco = cliente[self.banco]
        pacientes = banco[self.nome_collection]

        return pacientes


class PacienteSchema(Schema):
    _id = fields.Str()
    nome = fields.Str()
    idade = fields.Str()
    prioridade = fields.Str()
    status = fields.Str()
