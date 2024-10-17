from flask import Flask, jsonify
from config import Config
from models import db
from routes import init_routes
from flask_swagger_ui import get_swaggerui_blueprint
from swagger import swagger_template
from flask_cors import CORS  
app = Flask(__name__)
CORS(app) 
app.config.from_object(Config)
#inicializamos la bd
db.init_app(app)
init_routes(app)
#Configuracion de swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={ 'app_name': "API101"}
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)
@app.route('/')
def home():
    return {"message" : "Bienvenido a la API SQLAlchemy"}
@app.route('/static/swagger.json')
def swagger_json():
    return jsonify(swagger_template)


if __name__ == '__main__':
    app.run(debug=True)