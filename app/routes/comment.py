from flask import Flask, render_template, request, redirect, url_for, Blueprint,make_response,jsonify

import database as db



#product = Blueprint('product', __name__, template_folder=template_dir, url_prefix='/product')
comment = Blueprint('comment', __name__,  url_prefix='/api')



# Rutas de la aplicación
@comment.get('/comment/<id>')
def home(id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT u.nombre_usuario, c.comentario, c.fecha FROM comentarios c, usuario u WHERE u.id = c.id_user AND c.id_prod = %s"%(str(id),))
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()
    
    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    columnNames = [column[0] for column in cursor.description]  #
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))

    
    cursor.close()
  
    if insertObject == []:
        res = make_response('No hay ningun comentario aun', 404)
    else: res = make_response(insertObject,200)

    return res
    #return insertObject

# Ruta para guardar usuariosen la base de datos
@comment.post('/addComment')
def addComment():
    new_comment = request.get_json()
    id_prod = new_comment['id_prod']
    id_user = new_comment['id_user']
    comentario = new_comment['comentario']

    if id_prod and id_user and comentario:
        cursor = db.database.cursor()
        sql = "INSERT INTO comentarios (id_prod, id_user, comentario) VALUES (%s, %s, %s)"
        data = (id_prod,id_user,comentario)
        cursor.execute(sql, data)
        db.database.commit()
        cursor.close()
    return jsonify("data")

@comment.delete('/deleteComment/<string:id>')
def deleteComment(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM comentarios WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El comentario se ha eliminado correctamente"



@comment.put('/editComment/<string:id>')
def editProd(id):
    comentario = request.form['comentario']
   
    if comentario:
        cursor = db.database.cursor()
        sql = "UPDATE comentarios SET comentario = %s WHERE id = %s"
        data = (comentario,id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('comment.home'))

# if __name__ == "__main__":
#      app.run(debug=True,port=5000)
