from .models.prontuarios import ProntuarioSchema, Conexao
from flask import jsonify


class ListarProntuarios:
    
    def process(self):

        instancia = Conexao()
        pacientes = instancia.process()
        retorno = []
        
        for x in pacientes.find():
            retorno.append(x)

        lista = ProntuarioSchema().dump(retorno, many=True)

        return jsonify(lista)
