from flask import Blueprint, jsonify
from pymongo import MongoClient
import json
from .service import ListarProntuarios

# implementação do módulo prontuarios
prontuarios_v1 = Blueprint("prontuarios", __name__,
                           url_prefix="/v1/prontuarios")


@prontuarios_v1.route("/", methods=["GET"])
def index_v1():

    lista_prontuarios = ListarProntuarios()
    lista_prontuarios = lista_prontuarios.process()

    return lista_prontuarios


@prontuarios_v1.route("/", methods=["POST"])
def retornar_pacientes():
    # data = PacienteSchema().loads(request.data)

    # lista = [v for v in request.data]

    try:
        criacao_pacientes = CriarPaciente()
        criacao_pacientes.process(request.data)
    except NameError:
        return(NameError)

    return "Criado"


@prontuarios_v1.route("/", methods=["PUT"])
def criar_pacientes():
    data = PacienteSchema().loads(request.data)

    lista = [v for v in data]

    try:
        atualizar_pacientes = EditarPacientes()
        atualizar_pacientes.process(lista[0])
    except NameError:
        return(NameError)

    return "Atualizado"


@prontuarios_v1.route("/<id>", methods=["DELETE"])
def deletar_pacientes(id):
    try:
        deletar_paciente = DeletarPaciente()
        deletar_paciente.process(id)
    except NameError:
        return(NameError)

    return "Deletado"


@prontuarios_v1.route("/<id>", methods=["GET"])
def retornar_paciente_por_id(id):
    try:
        list_by_id = ListarPacientes()
        retorno_requisicao = list_by_id.process_by_id(id)
    except NameError:
        return(NameError)

    return retorno_requisicao
