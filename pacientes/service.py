from .models.pacientes import PacienteSchema, Conexao
from flask import jsonify


class ListarPacientes:
    
    def process(self):

        instancia = Conexao()
        pacientes = instancia.process()
        retorno = []
        
        for x in pacientes.find():
            retorno.append(x)

        lista = PacienteSchema().dump(retorno, many=True)

        return jsonify(lista)
