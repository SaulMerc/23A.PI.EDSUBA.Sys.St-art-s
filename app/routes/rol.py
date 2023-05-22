from flask import Flask, Blueprint, jsonify, request, make_response
import database as db

rol = Blueprint('rol', __name__,url_prefix='/api')

@rol.get('/rol/')
def getRol():
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM roles WHERE id != 1")
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
        res = make_response('No hay ningun rol aun', 404)
    else: res = make_response(insertObject,200)

    return res

@rol.post('/addRol/')
def addRol():
    new_category = request.get_json()
    rol = new_category['rol']
    descripcion = new_category['descripcion']

    if rol:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO roles (id, rol, descripcion) VALUES (NULL, %s, %s)"
        data = (rol,descripcion)
        cursor.execute(sql, data)
        db.database.commit()

        cursor.close()
        return jsonify({'mensaje':'Rol registrado con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})
     

@rol.delete("/deleteRol/<id>")
def deleteRol(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM roles WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El rol se ha eliminado correctamente"