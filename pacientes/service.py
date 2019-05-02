from .models.pacientes import PacienteSchema, Conexao


class ListarPacientes:
    def process(self):

        instancia = Conexao()
        pacientes = instancia.process()
        retorno = []
        
        for x in pacientes.find():
            retorno.append(x)

        print(retorno)
