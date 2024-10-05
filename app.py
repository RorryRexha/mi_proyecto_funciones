from flask import Flask
from db import db  # Importar db desde db.py
from routes.usuarios import usuarios_routes

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///102.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la app
db.init_app(app)

# Registrar las rutas
app.register_blueprint(usuarios_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas si no existen
    app.run(debug=True)
