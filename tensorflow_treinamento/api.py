import os
from flask import Blueprint, jsonify, make_response, request
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
    
    #self.estrutura_rede.__setattr__('value', estrutura_rede)
    classificador = model_from_json(estrutura_rede)
    classificador.load_weights('tensorflow_treinamento\classificador_breast.h5')

    #Uso em um registro
    #Passa um NP ARRAY para uma variável
    novo = np.array([[0.3, 0.2, 0.5, 0.6, 1, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7],[0.3, 0.2, 0.5, 0.6, 1, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7]])

    #Envia usar esta variável nesta linha de comando
    previsao =classificador.predict(novo)

    a = np.array(previsao).tolist()
   
    return json.dumps({"prediction": a})