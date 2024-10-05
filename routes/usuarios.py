from flask import Blueprint, request, jsonify
from controllers.usuarios_controller import obtener_usuarios, obtener_usuario_por_id, crear_usuario, actualizar_usuario, borrar_usuario


usuarios_routes = Blueprint('usuarios', __name__)

# Definir las rutas (GET, POST, PUT, DELETE) aquí
@usuarios_routes.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = obtener_usuarios()
    return jsonify([usuario.serialize() for usuario in usuarios])

@usuarios_routes.route('/api/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = obtener_usuario_por_id(id)
    if usuario:
        return jsonify(usuario.serialize())
    return jsonify({'message': 'Usuario no encontrado'}), 404

@usuarios_routes.route('/api/usuarios', methods=['POST'])
def post_usuario():
    data = request.get_json()
    if not data or not 'nombre' in data or not 'email' in data:
        return jsonify({'message': 'Datos incompletos'}), 400
    nuevo_usuario = crear_usuario(data)
    return jsonify(nuevo_usuario.serialize()), 201

@usuarios_routes.route('/api/usuarios/<int:id>', methods=['PUT'])
def put_usuario(id):
    data = request.get_json()
    if not data or not 'nombre' in data or not 'email' in data:
        return jsonify({'message': 'Datos incompletos'}), 400
    usuario_actualizado = actualizar_usuario(id, data)
    if usuario_actualizado:
        return jsonify(usuario_actualizado.serialize())
    return jsonify({'message': 'Usuario no encontrado'}), 404

@usuarios_routes.route('/api/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario_borrado = borrar_usuario(id)
    if usuario_borrado:
        return jsonify({'message': 'Usuario eliminado con éxito'})
    return jsonify({'message': 'Usuario no encontrado'}), 404
