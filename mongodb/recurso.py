from pymongo import MongoClient
import pymongo
import uuid
# from mock import mock_pacientes

id_carga = str(uuid.uuid4())


class Carga:

    def criar_base(self):
        banco = pymongo.MongoClient('localhost', 17017)
        criar_base = banco["tcc"]
        print("OK")

    def carga_pacientes(self):

        carga_pacientes = [
            {
                "nome": "Matheus",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Marcos",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Lucas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Judas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Thiago",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Pedro",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
            {
                "nome": "Paulo",
                "idade": "27",
                "prioridade": "Alta",
                "status": "Não Processado"
            },
        ]

        # conexao com o banco
        cliente = MongoClient('localhost', 17017)

        # selecionando o banco
        banco = cliente['tcc']

        # acessando a respectiva tabela
        prontuario = banco['pacientes']

        paciente_id = prontuario.insert_many(carga_pacientes)

        print("ok")

    def carga_prontuario(self):

        carga_prontuarios = [
            {
                "prontuario": {
                    "id_paciente": id_carga,
                    "nome": "teste",
                    "idade": 1,
                    "observacoes": "ABCDEFG",
                    "sintomas": [
                        {
                            "sintoma": "XPTO",
                            "grau": 0
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 1
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 2
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 3
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 4
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 5
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 5
                        },
                        {
                            "sintoma": "XPTO",
                            "grau": 5
                        }
                    ]
                }
            }
        ]

        # conexao com o banco
        cliente = MongoClient('localhost', 17017)

        # selecionando o banco
        banco = cliente['tcc']

        # acessando a respectiva tabela
        prontuario = banco['prontuarios']

        prontuario_id = prontuario.insert_many(carga_prontuarios)

        print("ok")

    def carga_doencas(self):

        # json com as doenças
        carga_doencas = [
            {
                "id": "1",
                "nome": "Matheus",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "2",
                "nome": "Marcos",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "3",
                "nome": "Lucas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "4",
                "nome": "Judas",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "5",
                "nome": "Thiago",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "6",
                "nome": "Pedro",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
            {
                "id": "7",
                "nome": "Paulo",
                "idade": "27",
                "prioridade": "Alta",
                "status": "OK"
            },
        ]

        # conexao com o banco
        cliente = MongoClient('localhost', 17017)

        # selecionando o banco
        banco = cliente['tcc']

        # acessando a respectiva tabela
        doenca = banco['doencas']

        doenca_id = prontuario.insert_many(carga_doencas)

        print("ok")
