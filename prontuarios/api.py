from flask import Blueprint, jsonify
from pymongo import MongoClient
import json
from .service import ListarProntuarios

# implementação do módulo prontuarios
prontuarios_v1 = Blueprint("prontuarios", __name__, url_prefix="/v1/prontuarios")


@prontuarios_v1.route("/")
def index_v1():

    lista_prontuarios = ListarProntuarios()
    lista_prontuarios = lista_prontuarios.process()

    return lista_prontuarios
