from flask import Flask
from flask_cors import CORS
from tensorflow import tensorflow_v1
from pytorch import pytorch_v1
from carga import carga_v1


app = Flask(__name__)

# implementação dos modulos
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(carga_v1)
app.register_blueprint(tensorflow_v1)
app.register_blueprint(pytorch_v1)

app.run(debug=True)
