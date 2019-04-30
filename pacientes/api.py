from flask import Blueprint, jsonify


#implementação do módulo pytorch
pacientes_v1 = Blueprint("pacientes",__name__,url_prefix="/v1/pacientes")


@pacientes_v1.route("/")
def index_v1():

    retorno = {"status":200}

    return jsonify(retorno)