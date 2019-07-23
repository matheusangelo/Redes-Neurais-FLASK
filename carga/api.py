import os
from flask import Blueprint, jsonify, make_response
from tensorboard import print_function
from mongodb import Carga

# implementação do blueprint do tensorflow
carga_v1 = Blueprint(
    "carga",
    __name__,
    url_prefix="/v1/carga")

resposta = {
    "status": 200
}


@carga_v1.route("/", methods=['OPTIONS'])
def options():
    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response


@carga_v1.route("/base")
def criar_base():
    carga = Carga()

    carga.criar_base()

    return jsonify(resposta)


@carga_v1.route("/pacientes")
def carga_pacientes():
    carga = Carga()

    carga.carga_pacientes()

    return jsonify(resposta)


@carga_v1.route("/prontuarios")
def carga_prontuarios():
    carga = Carga()

    carga.carga_prontuario()

    return jsonify(resposta)


@carga_v1.route("/doencas")
def carga_doencas():
    carga = Carga()

    carga.carga_doencas()

    return jsonify(resposta)
