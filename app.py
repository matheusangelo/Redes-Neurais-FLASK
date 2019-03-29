from flask import Flask
from tensorflow import tensorflow_v1
from pytorch import pytorch_v1


app = Flask(__name__)

#implementação dos modulos
app.register_blueprint(tensorflow_v1)
app.register_blueprint(pytorch_v1)

app.run(debug=True)