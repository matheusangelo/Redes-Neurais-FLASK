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
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "data_atendimento": "10/10/2010",
                "status": "Não Processado",
                "identificador": "SUS",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Marcos",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Lucas",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Judas",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Thiago",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Pedro",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
            },
            {
                "nome": "Paulo",
                "data_atendimento": "10/10/2010",
                "idade": "27",
                "rg": "48-885-333-9",
                "cpf": "407.777.768-02",
                "sexo": "Masculino",
                "identificador": "SUS",
                "status": "Não Processado",
                "observacoes": "usuario-carga",
                "status": False,
                "resultados": False,
                "inputs": {
                    "value1": 10,
                    "value2": 10,
                    "value3": 10,
                    "value4": 10,
                    "value5": 10,
                    "value6": 10,
                    "value7": 10,
                    "value8": 10,
                    "value9": 10,
                    "value10": 10,
                    "value11": 10,
                    "value12": 10,
                    "value13": 10,
                    "value14": 10,
                    "value15": 10,
                    "value16": 10,
                    "value17": 10,
                    "value18": 10,
                    "value19": 10,
                    "value20": 10,
                    "value21": 10,
                    "value22": 10,
                    "value23": 10,
                    "value24": 10,
                    "value25": 10,
                    "value26": 10,
                    "value27": 10,
                    "value28": 10,
                    "value29": 10,
                    "value30": 10,
                }
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

    def carga_auth(self):

        usuarios = [
            {
                "login": "admin",
                "senha": "admin",
                "profile": "especialista"
            }
        ]

        # conexao com o banco
        cliente = MongoClient('localhost', 17017)

        # selecionando o banco
        banco = cliente['tcc']

        # acessando a respectiva tabela
        prontuario = banco['usuarios']

        # prontuario_id = prontuario.insert_many(carga_prontuarios)

        print("ok")
