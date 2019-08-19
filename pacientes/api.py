from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from .service import Paciente
from . models import PacienteSchema

# implementação do módulo pacientes
pacientes_v1 = Blueprint("pacientes", __name__, url_prefix="/v1/pacientes")
_objPaciente = Paciente()


@pacientes_v1.route("/", methods=["GET"])
def index_v1():

    lista_pacientes = _objPaciente.process()

    return lista_pacientes


@pacientes_v1.route("/", methods=["POST"])
def retornar_pacientes():

    try:
        _objPaciente.process_criar(request.data)
    except NameError:
        return(NameError)

    return "Criado"


@pacientes_v1.route("/", methods=["PUT"])
def criar_pacientes():
    try:
        _objPaciente.process_editar(request.data)
    except NameError:
        return(NameError)

    return "Atualizado"


@pacientes_v1.route("/<id>", methods=["DELETE"])
def deletar_pacientes(id):
    try:
        _objPaciente.process_deletar(id)
    except NameError:
        return(NameError)

    return "Deletado"


@pacientes_v1.route("/<id>", methods=["GET"])
def retornar_paciente_por_id(id):
    try:
        retorno_requisicao = _objPaciente.process_by_id(id)
    except NameError:
        return(NameError)

    return retorno_requisicao
