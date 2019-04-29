import os
from flask import Blueprint, jsonify, make_response
from tensorboard import print_function
from mongodb import Conexao

#implementação do blueprint do tensorflow
carga_v1 = Blueprint(
    "carga",
    __name__,
    url_prefix="/v1/carga")


@carga_v1.route("/", methods=['OPTIONS'])
def options():
    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response

@carga_v1.route("/")
def index():
    resposta = {"status":200}

    return  jsonify(resposta)