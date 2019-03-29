from flask import Blueprint, jsonify


#implementação do módulo pytorch
pytorch_v1 = Blueprint("Pytorch",__name__,url_prefix="/v1/pytorch")


@pytorch_v1.route("/")
def index_v1():

    retorno = {"status":200}

    return jsonify(retorno)