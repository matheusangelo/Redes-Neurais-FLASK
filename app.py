from flask import Flask
from flask_cors import CORS
from tensorflow_treinamento import tensorflow_v1
from carga import carga_v1
from pacientes import pacientes_v1
from prontuarios import prontuarios_v1


app = Flask(__name__)

# implementação dos modulos
CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(carga_v1)
app.register_blueprint(pacientes_v1)
app.register_blueprint(prontuarios_v1)
app.register_blueprint(tensorflow_v1)


app.run(debug=True)
