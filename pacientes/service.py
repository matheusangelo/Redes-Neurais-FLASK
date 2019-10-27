from .models.pacientes import PacienteSchema, Conexao
from flask import jsonify
from bson.objectid import ObjectId


INDEX_DADOS = 0


class Paciente:
    def __init__(self):
        self.instancia = Conexao()
        self.pacientes = self.instancia.process()

    def process(self):

        retorno = []

        for paciente in self.pacientes.find():
            retorno.append(paciente)

        lista = PacienteSchema().dump(retorno, many=True)

        return jsonify(lista)

    def process_by_id(self, id):
        retorno = []

        for paciente in self.pacientes.find({"_id": ObjectId(id)}):
            retorno.append(paciente)

        lista = PacienteSchema().dump(retorno, many=True)

        return jsonify(lista[INDEX_DADOS])

    def process_criar(self, data):
        dados = PacienteSchema().loads(data)

        lista = [v for v in dados]
        
        insert = self.pacientes.insert_one(dados)

        return "ok"

    def process_deletar(self, id):
        delete = self.pacientes.delete_one({"_id": ObjectId(id)})

        return "ok"

    def process_editar(self, data,id):
        dados = PacienteSchema().loads(data)
        lista = [v for v in dados]

        data = lista[INDEX_DADOS]

        filtro = {"_id": ObjectId(id)}

        retorno = self.dict_update(dados)

        novos_valores = {"$set": retorno}


        self.pacientes.update_one(filtro, novos_valores)

        for x in self.pacientes.find():
            print(x)

        return "ok"

    def dict_update(self, data):
        dados = {
            "nome" : data['nome'],
            "idade" : data['idade'],
            "identificador" : data['identificador'],
            "data_atendimento" : data['data_atendimento'],
            "observacoes" : data['observacoes'],
            "rg" : data['rg'],
            "cpf" : data['cpf'],
            "sexo" : data['sexo'],
            "inputs": data['inputs'],
            "status": False,
            "resultado": False,
        }
        return dados