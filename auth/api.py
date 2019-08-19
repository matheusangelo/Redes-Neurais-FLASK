import os
from flask import Blueprint, jsonify, make_response
from tensorboard import print_function
from mongodb import Carga
import jwt

# implementação do jwt para autenticações na aplicação
auth_v1 = Blueprint(
    "auth",
    __name__,
    url_prefix="/v1/auth")

resposta = {
    "status": 200
}


@auth_v1.route("/", methods=['OPTIONS'])
def options():
    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response


@auth_v1.route("/", methods=["GET"])
def index_v1():

    lista_pacientes = _objPaciente.process()

    return lista_pacientes


@auth_v1.route("/", methods=["POST"])
def retornar_pacientes():

    try:
        _objPaciente.process_criar(request.data)
    except NameError:
        return(NameError)

    return "Criado"


@auth_v1.route("/", methods=["PUT"])
def criar_pacientes():
    try:
        _objPaciente.process_editar(request.data)
    except NameError:
        return(NameError)

    return "Atualizado"


@auth_v1.route("/<id>", methods=["DELETE"])
def deletar_pacientes(id):
    try:
        _objPaciente.process_deletar(id)
    except NameError:
        return(NameError)

    return "Deletado"


@auth_v1.route("/<id>", methods=["GET"])
def retornar_paciente_por_id(id):
    try:
        retorno_requisicao = _objPaciente.process_by_id(id)
    except NameError:
        return(NameError)

    return retorno_requisicao
