from .models.prontuarios import ProntuarioSchema, Conexao
from flask import jsonify
from bson.objectid import ObjectId

INDEX_DADOS = 0


class Prontuario:

    def __init__(self):
        self.instancia = Conexao()
        self.prontuarios = self.instancia.process()

    def process(self):

        retorno = []

        for prontuario in self.prontuarios.find():
            retorno.append(prontuario)

        lista = ProntuarioSchema().dump(retorno, many=True)

        return jsonify(lista)

    def process_by_id(self, id):
        retorno = []

        for paciente in self.prontuarios.find({"_id": ObjectId(id)}):
            retorno.append(paciente)

        lista = ProntuarioSchema().dump(retorno, many=True)

        return jsonify(lista[INDEX_DADOS])

    def process_criar(self, data):
        dados = ProntuarioSchema().loads(data)

        lista = [v for v in dados]

        insert = self.prontuarios.insert_one(lista[INDEX_DADOS])

        return "ok"

    def process_deletar(self, id):
        delete = self.prontuarios.delete_one({"_id": ObjectId(id)})

        return "ok"

    def process_editar(self, data):
        dados = ProntuarioSchema().loads(data)

        lista = [v for v in dados]

        data = lista[INDEX_DADOS]

        filtro = {"_id": ObjectId(data['_id'])}

        retorno = self.dict_update(data)

        novos_valores = {"$set": retorno}

        self.prontuarios.update_one(filtro, novos_valores)

        for x in self.prontuarios.find():
            print(x)

        return "ok"

    def dict_update(self, data):
        dados = {
            "idade": data["idade"],
            "nome": data["nome"],
            "prioridade": data["prioridade"],
            "status": data["status"]
        }
        return dados