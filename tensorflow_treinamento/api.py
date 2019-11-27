import os
from flask import Blueprint, jsonify, make_response, request
from .models.pacientes import PacienteSchema
from tensorboard import print_function
from mongodb import Carga
import numpy as np
import json
from keras.models import model_from_json
import pandas as pd


#implementação do blueprint do tensorflow
tensorflow_v1 = Blueprint(
    "tensorflow",
    __name__,
    url_prefix="/v1/tensorflow")


@tensorflow_v1.route("/", methods=['OPTIONS'])
def options():
    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response

@tensorflow_v1.route("/teste", methods=['POST'])
def index():
    arquivo = open('tensorflow_treinamento\classificador_breast.json','r')
    estrutura_rede = arquivo.read()
    arquivo.close()

    classificador = model_from_json(estrutura_rede)
    classificador.load_weights('tensorflow_treinamento\classificador_breast.h5')
    print("\n\n\n\n\n\n","Depois","\n\n\n\n\n\n")
    dados = PacienteSchema().loads(request.data)
    entradas = dados['lista']
    print("\n\n\n\n\n\n","dados","\n\n\n\n\n\n")
    
    matrix_entrada = []
    matrix_entrada.append(entradas)

    print("\n\n\n\n\n", matrix_entrada,"\n\n\n\n\n")
    #Uso em um registro
    #Passa um NP ARRAY para uma variável
    novo = np.array(matrix_entrada)

    #Envia usar esta variável nesta linha de comando
    previsao =classificador.predict(novo)

    a = np.array(previsao).tolist()

    if  previsao > 0.5:
        a = "Positivo"
    else:
        a = "Negativo"
    
    return json.dumps({"prediction":a})