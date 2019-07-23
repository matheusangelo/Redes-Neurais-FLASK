from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import json
from .service import Doenca

# implementação do módulo prontuarios
doencas_v1 = Blueprint("doencas", __name__,
                           url_prefix="/v1/doencas")

_objDoencas = Doenca()


@doencas_v1.route("/listar", methods=["GET"])
def index_v1():

    lista_pacientes = _objDoencas.process()

    return lista_pacientes


@doencas_v1.route("/criar", methods=["POST"])
def retornar_pacientes():
    try:
        _objDoencas.process_criar(request.data)
    except NameError:
        return(NameError)

    return "Criado"


@doencas_v1.route("/editar", methods=["PUT"])
def criar_pacientes():
    try:
        _objDoencas.process_editar(request.data)
    except NameError:
        return(NameError)

    return "Atualizado"


@doencas_v1.route("/<id>", methods=["DELETE"])
def deletar_pacientes(id):
    try:
        _objDoencas.process_deletar(id)
    except NameError:
        return(NameError)

    return "Deletado"


@doencas_v1.route("/<id>", methods=["GET"])
def retornar_paciente_por_id(id):
    try:
        retorno_requisicao = _objDoencas.process_by_id(id)
    except NameError:
        return(NameError)

    return retorno_requisicao
