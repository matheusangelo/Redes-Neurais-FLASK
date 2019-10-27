from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from .service import Prontuario

# implementação do módulo prontuarios
prontuarios_v1 = Blueprint("prontuarios", __name__,
                           url_prefix="/v1/prontuarios")

_objProntuario = Prontuario()


@prontuarios_v1.route("/", methods=["GET"])
def index_v1():

    lista_pacientes = _objProntuario.process()

    return lista_pacientes


@prontuarios_v1.route("/", methods=["POST"])
def retornar_pacientes():
    try:
        print(request.data)
        _objProntuario.process_criar(request.data)
    except NameError:
        return(NameError)

    return  jsonify({"status":200})


@prontuarios_v1.route("/", methods=["PUT"])
def criar_pacientes():
    try:
        _objProntuario.process_editar(request.data)
    except NameError:
        return(NameError)

    return jsonify({"status":200})

@prontuarios_v1.route("/<id>", methods=["DELETE"])
def deletar_pacientes(id):
    try:
        _objProntuario.process_deletar(id)
    except NameError:
        return(NameError)

    return "Deletado"


@prontuarios_v1.route("/<id>", methods=["GET"])
def retornar_paciente_por_id(id):
    try:
        retorno_requisicao = _objProntuario.process_by_id(id)
    except NameError:
        return(NameError)

    return retorno_requisicao
