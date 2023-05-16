from flask import Flask, Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import database as db

user = Blueprint('api', __name__,url_prefix='/api')

@user.get('/users/')
def getUsers():
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("select u.*, r.rol from usuario u, roles r where u.id_rol = r.id and r.id = 1")
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()
    
   
    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    
    columnNames = [column[0] for column in cursor.description] 
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))
        #insertObject
    #Cerrar conexion
    cursor.close()

    if insertObject == []:
        res = make_response('No hay ningun usuario aun', 404)
    else: res = make_response(insertObject,200)

    return res


@user.get('/user/<id>')
def getUserById(id=id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("select * from usuario where usuario.id = %s"%(str(id),))
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()
    
    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    
    columnNames = [column[0] for column in cursor.description] 
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))
        #insertObject
    #Cerrar conexion
    cursor.close()

    if insertObject == []:
        res = make_response('No se encontro al usuario', 404)
    else: res = make_response(insertObject,200)

    return res
    

@user.post('/userI/')
def addUser():
    new_user = request.get_json()
    nombre = new_user['nombre']
    correo = new_user['correo']
    contrasena = generate_password_hash(new_user['contrasena'], method="pbkdf2:sha256")
    nombre_usuario = new_user['nombre_usuario']
    f_nacimiento = new_user['f_nacimiento']
    numero_tel = new_user['numero_tel']

    

    if nombre and correo and contrasena and nombre_usuario and f_nacimiento and numero_tel:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuario (id, nombre, correo, nombre_usuario, f_nacimiento, numero_tel, id_rol) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
        data = (nombre, correo, nombre_usuario, f_nacimiento, numero_tel, 1)
        cursor.execute(sql, data)
        db.database.commit()
        respuesta = data
        # Obtener el último ID insertado
        last_insert_id = cursor.lastrowid
        print(last_insert_id)
        #Insersión de la contraseña del usuario
        cursor = db.database.cursor()
        sql = "INSERT INTO contrasenas (id_usuario, contrasena) VALUES (%s, %s)"
        data = (last_insert_id, contrasena)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
        respuesta = respuesta + data
        return jsonify(respuesta)

# ////////////////////////////////////////////////

@user.post("/useru/<id>")
def updateUser(id=str(id)):
    update_user = request.get_json()
    nombre = update_user['nombre']
    correo = update_user['correo']
    nombre_usuario = update_user['nombre_usuario']
    f_nacimiento = update_user['f_nacimiento']
    numero_tel = update_user['numero_tel']
    

    if nombre and correo and nombre_usuario and f_nacimiento and numero_tel and id:
        cursor = db.database.cursor()
        sql = "UPDATE usuario SET nombre = %s, correo = %s, nombre_usuario = %s, f_nacimiento = %s, numero_tel = %s WHERE id = %s"
        data = (nombre, correo, nombre_usuario, f_nacimiento, numero_tel, id)
        cursor.execute(sql, data)
        db.database.commit()
        resp=make_response(jsonify(data), 200)
    
    else: resp=make_response('Algo salio mal, revisa los datos...',400)

    return resp


@user.delete("/deleteuser/<id>")
def deleteUser(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM usuario WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El usuario se ha eliminado correctamente"