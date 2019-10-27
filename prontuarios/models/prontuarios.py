from pymongo import MongoClient
from marshmallow import fields, Schema


class Conexao:

    def process(self):
        cliente = MongoClient('localhost', 17017)
        banco = cliente['tcc']
        prontuario = banco['prontuarios']

        return prontuario


class SintomasSchema(Schema):
    chave = fields.Str()
    valor = fields.Int()


class ProntuarioSchema(Schema):
    _id = fields.Str()
    idade = fields.Str()
    idenficador = fields.Str()
    nome = fields.Str()
    sexo = fields.Str()
    sintomas = fields.List(fields.Nested(SintomasSchema))
