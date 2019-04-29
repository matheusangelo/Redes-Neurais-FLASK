from pymongo import MongoClient


class Conexao:

    def process(self):
        #conexao com o banco
        cliente = MongoClient('localhost', 17017)

        #selecionando o banco
        banco = cliente['pacientes']

        #acessando a respectiva tabela
        prontuario = banco['prontuario']

        print(prontuario)