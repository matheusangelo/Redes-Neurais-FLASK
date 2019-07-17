from flask import Blueprint, jsonify
from pymongo import MongoClient
import json
from .service import ListarPacientes

# implementação do módulo pacientes
pacientes_v1 = Blueprint("pacientes", __name__, url_prefix="/v1/pacientes")


@pacientes_v1.route("/")
def index_v1():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return lista_pacientes


@pacientes_v1.route("/", methods=["POST"])
def retornar_pacientes():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return lista_pacientes


@pacientes_v1.route("/", methods=["PUT"])
def criar_pacientes():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return 


@pacientes_v1.route("/", methods=["DELETE"])
def deletar_pacientes():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return 200


@pacientes_v1.route("/", methods=["GET"])
def retornar_paciente_por_id():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return lista_pacientes