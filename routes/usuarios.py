from flask import Blueprint, request, jsonify

from controllers.usuarios_controller import obtener_usuario
from controllers.usuarios_controller import crear_usuario


usuarios_routes = Blueprint('usuarios',__name__)

@usuarios_routes.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = obtener_usuario()
    return jsonify(usuarios)


@usuarios_routes.route('/api/usuarios', methods=['POST'])
def post_usuario():
    data = request.get_json()  
    nuevo_usuario = crear_usuario(data) 
    if nuevo_usuario:
        return jsonify({'message': 'Usuario creado con éxito', 'usuario': nuevo_usuario}), 201
    else:
        return jsonify({'message': 'Error al crear usuario'}), 400