# Ambiente

1. [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. [virtualenv](https://virtualenv.pypa.io/en/stable/)
3. [Docker](https://www.docker.com/)


## Instalando dependências do ambiente de dev

### Criar ambiente

`virtualenv .venv`

#### Ativar ambiente no Windows

`.venv/Scripts/activate.bat`

#### Ativar ambiente no Linux

`source .venv/bin/activate`

### Instalar dependências

`pip install -r requirements.txt`

##MongoDB

`docker pull mongo`

`docker run --name tcc -p 17017:27017 -d mongo`


## Instalando Tensorflow
- `pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`

## Instalando Pytorch
- `pip3 install https://download.pytorch.org/whl/cu90/torch-1.0.1-cp36-cp36m-win_amd64.whl`
-  `pip3 install torchvision`
