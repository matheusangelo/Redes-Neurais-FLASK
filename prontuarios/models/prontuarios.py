from pymongo import MongoClient
from marshmallow import fields, Schema


class Conexao:

    def process(self):
        cliente = MongoClient('localhost', 17017)
        banco = cliente['tcc']
        prontuario = banco['prontuarios']

        return prontuario


class ProntuarioSchema(Schema):
    _id = fields.Str()
    nome = fields.Str()
    idade = fields.Str()
    prioridade = fields.Str()
    status = fields.Str()
