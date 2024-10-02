from db  import get_db_connection

def obtener_usuario():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql ="SELECT id, nombre, email FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    connection.close()
    return usuarios



def crear_usuario(data):
    try:
       
        usuario = {
            'id': 1,
            'nombre': data['nombre'],
            'email': data['email']
        }
        return usuario  
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return None
