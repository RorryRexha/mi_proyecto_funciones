from db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email
        }
