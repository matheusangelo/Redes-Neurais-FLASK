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


class PacienteSchema(Schema):
    _id = fields.Str()
    nome = fields.Str()
    idade = fields.Str()
    sexo = fields.Str()
    prioridade = fields.Str()
    status = fields.Str()


# {
# 	_id:
# 	nome_paciente:
# 	idade:
# 	rg:
# 	cpf:
# 	sexo:
# 	identificador:
# 	dt_atendimento:
# 	observacoes:
# 	avaliacao: [
# 		sintomas:
# 		intensidade:
# 	]
# }