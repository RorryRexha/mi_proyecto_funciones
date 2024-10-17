from flask import request
from models import db
from models.usuarios import Usuario
#commit  => guardado de informacion 
def obtener_usuario():
    return Usuario.query.all()
def usuario_por_id(id):
    return Usuario.query.get(id)  
def agregar_usuario(data):
    nuevo_usuario = Usuario(nombre= data['nombre'], email= data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado correctamente"
def actualizar_usuario(id, data):
    usuario = Usuario.query.get(id)
    if 'nombre' in data:
        usuario.nombre = data['nombre']
    if 'email' in data:
        usuario.email = data['email']
    db.session.commit()
    return "Usuario actualizado correctamente"
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Usuario eliminado correctamente"