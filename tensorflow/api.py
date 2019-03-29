import os
from flask import Blueprint, jsonify
from tensorboard import print_function

#implementação do blueprint do tensorflow
tensorflow_v1 = Blueprint(
    "tensorflow",
    __name__,
    url_prefix="/v1/tensorflow")

@tensorflow_v1.route("/")
def index():

    resposta = {"status":200}

    return  jsonify(resposta)