from models.usuarios import Usuario
from db import db


def obtener_usuarios():
    return Usuario.query.all()

def obtener_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def crear_usuario(data):
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return nuevo_usuario

def actualizar_usuario(usuario_id, data):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        usuario.nombre = data['nombre']
        usuario.email = data['email']
        db.session.commit()
        return usuario
    return None

def borrar_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return usuario
    return None
