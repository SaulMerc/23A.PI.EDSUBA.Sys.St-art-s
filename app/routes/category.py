from flask import Flask, Blueprint, jsonify, request, make_response
import database as db

category = Blueprint('category', __name__,url_prefix='/api')

@category.get('/category/')
def getCategory(): 
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM categoria")
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
        res = make_response('No hay ninguna categoria aun', 404)
    else: res = make_response(insertObject,200)

    return res

@category.post('/addCategory/')
def addCategory():
    new_category = request.get_json()
    categoria = new_category['categoria']

    if categoria:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO categoria (id, categoria) VALUES (NULL, %s)"
        data = (categoria,)
        cursor.execute(sql, data)
        db.database.commit()

        cursor.close()
        return jsonify({'mensaje':'Categoria registrado con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})
     

@category.delete("/deleteCategory/<id>")
def deleteCategory(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM categoria WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "La categoria se ha eliminado correctamente"