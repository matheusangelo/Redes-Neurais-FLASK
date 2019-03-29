# Ambiente

1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [Docker](https://www.docker.com/)
4. [DynamoDB]()

## Instalando dependências do ambiente de dev

### Criar ambiente

`virtualenv .venv`

#### Ativar ambiente no Windows

`.venv/Scripts/activate.bat`

#### Ativar ambiente no Linux

`source .venv/bin/activate`

### Instalar dependências

`pip install -r requirements.txt`

## DynamoDB Local

Para rodar o DynamoDB localmente, é preciso realizar o download

- [AWS Developer Guide - DynamoDB Local](https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/DynamoDBLocal.html)

Após o download, extrair em um diretório, e utilizar o comando:

- `java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb`

## Health Check e Ambiente

Para acessar o status da API, foi disponiblizado o endpoint `/healhcheck`
Exemplo de retorno:

```json
{
    hostname: "localhost",
    status: "success",
    timestamp: 1540318049.0074956,
    results: []
}
```

## Instalando Tensorflow
- `pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`

## Instalando Pytorch
- `pip3 install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp36-cp36m-win_amd64.whl`
-  `pip3 install torchvision`
