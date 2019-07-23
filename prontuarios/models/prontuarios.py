from pymongo import MongoClient
from marshmallow import fields, Schema


class Conexao:

    def process(self):
        cliente = MongoClient('localhost', 17017)
        banco = cliente['tcc']
        prontuario = banco['prontuarios']

        return prontuario


class SintomasSchema(Schema):
    sintoma = fields.Str()
    grau = fields.Int()


class ProntuarioSchema(Schema):
    _id = fields.Str()
    id_paciente = fields.Str()
    sintomas = fields.List(fields.Nested(SintomasSchema))
