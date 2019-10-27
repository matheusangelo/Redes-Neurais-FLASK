# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:15:32 2019

@author: firanzi
"""
import numpy as np
from keras.models import model_from_json
import pandas as pd

class RedeNeural:
    def ProcessarRede(self):
        arquivo = open('tensorflow_treinamento\classificador_breast.json','r')
        estrutura_rede = arquivo.read()
        arquivo.close()

        help(self)
        #self.estrutura_rede.__setattr__('value', estrutura_rede)
        classificador = model_from_json(estrutura_rede)
        classificador.load_weights('tensorflow_treinamento\classificador_breast.h5')

        #Uso em um registro
        #Passa um NP ARRAY para uma variável
        novo = np.array([[0.3, 0.2, 0.5, 0.6, 1, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7],[0.3, 0.2, 0.5, 0.6, 1, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7,0.3, 0.2, 0.5, 0.6, 0.7, 0.1, 0.5, 0.3, 1, 0.7]])

        #Envia usar esta variável nesta linha de comando
        previsao = classificador.predict(novo)

        print("\n\n\n\n\n",previsao,"\n\n\n\n\n\n\n")

        return "ok"

