from flask import Flask, Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import database as db

user = Blueprint('user', __name__,url_prefix='/api')

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

@user.post("/login")
def login():
  if request.method == "POST":
    new_user = request.json
    correo = new_user['correo']
    contrasena = new_user['contrasena']

    cursor = db.database.cursor()
    cursor.execute(f"SELECT u.id, c.contrasena FROM usuario u, contrasenas c WHERE u.correo = '{correo}' AND u.id = c.id_usuario")

    myresult = cursor.fetchall()

    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    
    columnNames = [column[0] for column in cursor.description] 
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))

    # Cerrar conexión
    cursor.close()

    print(insertObject)

    if check_password_hash(insertObject[0]['contrasena'], contrasena):
        return jsonify(insertObject[0]['id'])
    else:
        res = make_response('No se encontro al usuario', 404)
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
    

@user.post('/addUser/')
def addUser():
    new_user = request.get_json()
    nombre = new_user['nombre']
    correo = new_user['correo']
    contrasena = generate_password_hash(new_user['contrasena'], method="pbkdf2:sha256")
    nombre_usuario = new_user['nombre_usuario']
    f_nacimiento = new_user['f_nacimiento']
    numero_tel = new_user['numero_tel']
    acerca_mi = new_user['acerca_mi']

    if nombre and correo and contrasena and nombre_usuario and f_nacimiento and numero_tel:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuario (id, nombre, correo, nombre_usuario, f_nacimiento, numero_tel, acerca_mi, id_rol) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"
        data = (nombre, correo, nombre_usuario, f_nacimiento, numero_tel, acerca_mi, 1)
        cursor.execute(sql, data)
        db.database.commit()
        respuesta = data
        # Obtener el último id que se insertó en la tabla
        last_insert_idUser = cursor.lastrowid
        #Insersión de la contraseña del usuario
        cursor = db.database.cursor()
        sql = "INSERT INTO contrasenas (id_usuario, contrasena) VALUES (%s, %s)"
        data = (last_insert_idUser, contrasena)
        cursor.execute(sql, data)
        db.database.commit()
        respuesta = respuesta + data

        #Insersión de la contraseña del usuario
        cursor = db.database.cursor()
        sql = "INSERT INTO `carrito` (`id`, `vendido`, `fecha_vendido`) VALUES (NULL, 'no', CURRENT_TIMESTAMP)"
        cursor.execute(sql)
        db.database.commit()
        
        # Obtener el último ID insertado
        last_insert_id = cursor.lastrowid
        #Insersión de la contraseña del usuario
        cursor = db.database.cursor()
        sql = "INSERT INTO `rel_user_car` (`id_user`, `id_car`) VALUES (%s, %s) "
        data = (last_insert_idUser, last_insert_id)
        cursor.execute(sql, data)
        db.database.commit()

        cursor.close()
        return jsonify({'mensaje':'Usuario registrado con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})




@user.put("/updateUser/<id>")
def updateUser(id=str(id)):
    update_user = request.get_json()
    nombre = update_user['nombre']
    correo = update_user['correo']
    nombre_usuario = update_user['nombre_usuario']
    f_nacimiento = update_user['f_nacimiento']
    numero_tel = update_user['numero_tel']
    acerca_mi = update_user['acerca_mi']

    if nombre and correo and nombre_usuario and f_nacimiento and numero_tel and id:
 
        cursor = db.database.cursor()
        sql = "UPDATE usuario SET nombre = %s, correo = %s, nombre_usuario = %s, f_nacimiento = %s, numero_tel = %s , acerca_mi = %s WHERE id = %s"
        data = (nombre, correo, nombre_usuario, f_nacimiento, numero_tel, acerca_mi, id)
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


@user.get('/direccion/<id>')
def getDireccion():
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("select d.*, u.nombre_usuario from usuario u, direccion d where d.id_user = u.id and u.id = %s"%(str(id),))
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

# id de usuario
@user.post('/addDireccion/<id>')
def addDireccion(id): 
    new_direccion = request.get_json()
    colonia = new_direccion['colonia']
    cod_postal = new_direccion['cod_postal']
    municipio = new_direccion['municipio']
    calle = new_direccion['calle']
    num_ext_int = new_direccion['num_ext_int']
    
    if colonia and cod_postal and municipio and calle and num_ext_int:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO direccion (id_user, colonia, cod_postal, municipio, calle, num_ext_int) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (id,colonia,cod_postal,municipio,calle, num_ext_int)
        cursor.execute(sql, data)
        db.database.commit()

        return jsonify({'mensaje':'Dirección registrada con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})

#id de la dirección
@user.put("/updateDireccion/<string:id>")
def updateDireccion(id):
    update_direccion = request.get_json()
    colonia = update_direccion['colonia']
    cod_postal = update_direccion['cod_postal']
    municipio = update_direccion['municipio']
    calle = update_direccion['calle']
    num_ext_int = update_direccion['num_ext_int']
    
    if colonia and cod_postal and municipio and calle and num_ext_int:
       
        cursor = db.database.cursor()
        sql = "UPDATE direccion SET colonia = %s, cod_postal = %s, municipio = %s, calle = %s, num_ext_int = %s WHERE direccion.id = %s"
        data = (colonia, cod_postal, municipio, calle, num_ext_int, id)
        cursor.execute(sql, data)
        db.database.commit()
        resp = make_response(jsonify(data), 200)
    else:
        resp = make_response('Algo salió mal, revisa los datos...', 400)

    return resp

#id de la dirección
@user.delete("/deleteDireccion/<string:id>")
def deleteDireccion(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM direccion WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "La dirección se ha eliminado correctamente"     

############## Crud de tarjeta ############
#id	id_user	num_tarjeta	nombre	


#id del usuario
@user.get('/getCard/<id>')
def getCard(id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor() 
    # ya las voy calando? ti
    cursor.execute("select t.*, u.nombre_usuario from usuario u, met_pago t where t.id_user = u.id and u.id = %s"%(str(id),))
   
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


@user.post('/addCard/<string:id>')
def addCard(id): 
    new_card = request.get_json()
    num_tarjeta = new_card['num_tarjeta']
    nombre = new_card['nombre']
    # es tarjeta o metodo de pago? va
    #met_pago    no llega id_user??
    if num_tarjeta and nombre:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO met_pago (id_user, num_tarjeta, nombre) VALUES (%s, %s, %s)"
        data = (id,num_tarjeta,nombre)
        cursor.execute(sql, data)
        db.database.commit()

        return jsonify({'mensaje':'Tarjeta registrada con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})

#id de la dirección
@user.put("/updateCard/<string:id>")
def updateCard(id):
    update_card = request.get_json()
    num_tarjeta =  update_card['num_tarjeta']
    nombre = update_card ['nombre']
    
    if num_tarjeta and nombre:
       
        cursor = db.database.cursor()
        sql = "UPDATE met_pago SET num_tarjeta = %s, nombre = %s WHERE met_pago.id = %s"
        data = (num_tarjeta, nombre, id)
        cursor.execute(sql, data)
        db.database.commit()
        resp = make_response(jsonify(data), 200)
    else:
        resp = make_response('Algo salió mal, revisa los datos...', 400)

    return resp

#id del met_pago
@user.delete("/deleteCard/<string:id>")
def deleteCard(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM met_pago WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "La tarjeta se ha eliminado correctamente"     
