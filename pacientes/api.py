from flask import Blueprint, jsonify
from pymongo import MongoClient
import json
from .service import ListarPacientes

# implementação do módulo pytorch
pacientes_v1 = Blueprint("pacientes", __name__, url_prefix="/v1/pacientes")


@pacientes_v1.route("/")
def index_v1():

    lista_pacientes = ListarPacientes()
    lista_pacientes = lista_pacientes.process()

    return lista_pacientes
