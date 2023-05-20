from flask import Flask, render_template, request, redirect, jsonify ,url_for, Blueprint,make_response
import os
import database as db




car = Blueprint('car', __name__,url_prefix='/api')

id_user = ""
# Rutas de la aplicación


@car.get('/getCar/<string:id>')
def home(id):
    global id_user
    id_user = id
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT ruc.id_user, u.nombre, c.id, c.vendido, c.fecha_vendido, p.titulo, p.precio FROM usuario u, carrito c, productos p, rel_user_car ruc, rel_car_prod rcp WHERE ruc.id_car = c.id AND rcp.id_car = c.id AND rcp.id_prod = p.id AND ruc.id_user = u.id AND u.id = %s",(id,))
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
        res = make_response('No hay ningun carrito aun', 404)
    else: res = make_response(insertObject,200)

    return res



@car.post('/addCar/<string:id>')
def addCar(id):
    if id:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO `carrito` (`id`, `vendido`, `fecha_vendido`) VALUES (NULL, 'no', CURRENT_TIMESTAMP)"
        cursor.execute(sql)
        db.database.commit()

        # Obtener el último ID insertado
        last_insert_id = cursor.lastrowid

        # Insertar en otra tabla utilizando el último ID
        cursor = db.database.cursor()
        sql = "INSERT INTO `rel_user_car` (`id_user`, `id_car`) VALUES (%s, %s) "
        data = (id, last_insert_id)
        cursor.execute(sql, data)
        db.database.commit()

        return jsonify({'mensaje':'Carrito creado con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})


@car.delete('/deleteCar/<string:id>')
def deleteCar(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM carrito WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El carrito se ha eliminado correctamente"



@car.put('/editCar/<string:id>')
def editCar(id):
    update_car = request.get_json()
    vendido = update_car['vendido']
    global id_user
    if vendido:
        cursor = db.database.cursor()
        sql = "UPDATE carrito SET vendido = %s WHERE id = %s"
        data = (vendido, id)
        cursor.execute(sql, data)
        db.database.commit()
        resp=make_response(jsonify(data), 200)
    
    else: resp=make_response('Algo salio mal, revisa los datos...',400)

    return resp
 




   