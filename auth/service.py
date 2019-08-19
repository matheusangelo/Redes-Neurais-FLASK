from .models.usuarios import UsuarioSchema, Conexao
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

        lista = UsuarioSchema().dump(retorno, many=True)

        return jsonify(lista)

    def process_by_id(self, id):
        retorno = []

        for paciente in self.pacientes.find({"_id": ObjectId(id)}):
            retorno.append(paciente)

        lista = UsuarioSchema().dump(retorno, many=True)

        return jsonify(lista[INDEX_DADOS])

    def process_criar(self, data):
        dados = UsuarioSchema().loads(data)

        lista = [v for v in dados]

        insert = self.pacientes.insert_one(lista[INDEX_DADOS])

        return "ok"

    def process_deletar(self, id):
        delete = self.pacientes.delete_one({"_id": ObjectId(id)})

        return "ok"

    def process_editar(self, data):
        dados = UsuarioSchema().loads(data)

        lista = [v for v in dados]

        data = lista[INDEX_DADOS]

        filtro = {"_id": ObjectId(data['_id'])}

        retorno = self.dict_update(data)

        novos_valores = {"$set": retorno}

        self.pacientes.update_one(filtro, novos_valores)

        for x in self.pacientes.find():
            print(x)

        return "ok"

    def dict_update(self, data):
        dados = {
            "nome": data["nome"],
            "usuario": data["usuario"],
            "senha": data["senha"],
            "email": data["email"]
        }
        return dados
