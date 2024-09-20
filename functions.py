from flask import Flask,  request, jsonify
                
import pymysql
import pymysql.cursors

app = Flask(__name__)

# functions.py
def function():
    print("This is function.")

def function1():
    print("This is function1.")

def function2():
    print("This is function2.")

def function3():
    print("This is function3.")


# Función para obtener la conexión a la base de datos
def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='101',
        cursorclass=pymysql.cursors.DictCursor)
    return connection

# Ruta GET para obtener los usuarios
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, nombre, email FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    connection.close()
    return jsonify(usuarios)

# Ruta POST para guardar los datos de un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def add_usuario():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    nombre = data.get('nombre')
    email = data.get('email')
    
    if not nombre or not email:
        return jsonify({'error': 'Datos incompletos'}), 400

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, email))
        connection.commit()  # Confirmar la transacción
        response = {'message': 'Usuario añadido exitosamente'}
    except Exception as e:
        connection.rollback()  # En caso de error, revertir la transacción
        response = {'error': str(e)}
    finally:
        connection.close()
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)