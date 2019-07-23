from .models.prontuarios import ProntuarioSchema, Conexao
from flask import jsonify


class ListarProntuarios:
    
    def process(self):

        instancia = Conexao()
        pacientes = instancia.process()
        retorno = []
        
        for x in pacientes.find():
            retorno.append(x)

        lista = ProntuarioSchema().dump(retorno, many=True)

        return jsonify(lista)


# class ListarPacientes:

#     def process(self):
#         instancia = Conexao()
#         pacientes = instancia.process()
#         retorno = []

#         for paciente in pacientes.find():
#             retorno.append(paciente)

#         lista = PacienteSchema().dump(retorno, many=True)

#         return jsonify(lista)

#     def process_by_id(self, id):
#         instancia = Conexao()
#         pacientes = instancia.process()
#         retorno = []

#         for paciente in pacientes.find({"_id":ObjectId(id)}):
#             retorno.append(paciente)

#         lista = PacienteSchema().dump(retorno, many=True)

#         return jsonify(lista[0])


# class CriarPaciente:

#     def process(self, data):
#         instancia = Conexao()
#         pacientes = instancia.process()
#         insert = pacientes.insert_one(data)

#         return "ok"


# class DeletarPaciente:

#     def process(self, id):
#         instancia = Conexao()
#         pacientes = instancia.process()
#         delete = pacientes.delete_one({"_id":ObjectId(id)})

#         return "ok"


# class EditarPacientes:

#     def process(self, data):
#         instancia = Conexao()
#         pacientes = instancia.process()

#         filtro = {"_id": ObjectId(data['_id'])}

#         retorno = self.dict_update(data)

#         novos_valores = {"$set": retorno}

#         pacientes.update_one(filtro, novos_valores)

#         for x in pacientes.find():
#             print(x)

#         return "ok"

#     def dict_update(self, data):
#         dados = {
#             "idade": data["idade"],
#             "nome": data["nome"],
#             "prioridade": data["prioridade"],
#             "status": data["status"]
#         }
#         return dados
