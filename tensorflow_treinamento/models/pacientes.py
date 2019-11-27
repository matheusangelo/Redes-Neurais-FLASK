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
        pacientes = banco["pacientes"]

        return pacientes


class InputsSchema(Schema):
    value1 = fields.Float()
    value2 = fields.Float()
    value3 = fields.Float()
    value4 = fields.Float()
    value5 = fields.Float()
    value6 = fields.Float()
    value7 = fields.Float()
    value8 = fields.Float()
    value9 = fields.Float()
    value10 = fields.Float()
    value11 = fields.Float()
    value12 = fields.Float()
    value13 = fields.Float()
    value14 = fields.Float()
    value15 = fields.Float()
    value16 = fields.Float()
    value17 = fields.Float()
    value18 = fields.Float()
    value19 = fields.Float()
    value20 = fields.Float()
    value21 = fields.Float()
    value22 = fields.Float()
    value23 = fields.Float()
    value24 = fields.Float()
    value25 = fields.Float()
    value26 = fields.Float()
    value27 = fields.Float()
    value28 = fields.Float()
    value29 = fields.Float()
    value30 = fields.Float()


class PacienteSchema(Schema):
    _id = fields.Str()
    nome = fields.Str()
    idade = fields.Str()
    identificador = fields.Str()
    data_atendimento = fields.Str()
    observacoes = fields.Str()
    rg = fields.Str()
    cpf = fields.Str()
    sexo = fields.Str()
    status = fields.Str()
    resultado = fields.Str()
    inputs = fields.Nested(InputsSchema)
    lista = fields.List(fields.Float())
