from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint,make_response
import database as db

product = Blueprint('product', __name__, url_prefix='/api')


# Rutas de la aplicación
@product.get('/getproducts')
def getProducts():
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM productos")
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()

    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    columnNames = [column[0] for column in cursor.description]  #
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))

    # Cerrar el cursor y devolver una plantilla HTML
    cursor.close()
    if insertObject == []:
        res = make_response('No hay ningun producto aun', 404)
    else: res = make_response(insertObject,200)

    return res

@product.get('/getproductid/<id>')
def getProductById(id=id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT DISTINCT p.*, i.imagen, u.nombre_usuario FROM productos p, imagenes i, usuario u WHERE u.id = p.id_user AND i.id_prod = p.id AND p.id = %s"%(str(id),))
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()

    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    columnNames = [column[0] for column in cursor.description]  #
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))

    # Cerrar el cursor y devolver una plantilla HTML
    cursor.close()
    if insertObject == []:
        res = make_response("No se encontró ese producto", 404)
    else: res = make_response(insertObject,200)

    return res

# Obtener producto por id de usuario
@product.get('/getproductuser/<id>')
def getProductByUserId(id=id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT DISTINCT p.*, i.imagen, u.nombre_usuario FROM productos p, usuario u, imagenes i WHERE p.id = i.id_prod AND p.id_user = u.id AND u.id = %s"%(str(id),))
    # cursor.execute("SELECT * FROM usuario")
    # Obtener todos los resultados de la consulta
    myresult = cursor.fetchall()

    # Convertir los resultados en un diccionario
    insertObject = []  # Crear una lista vacía para almacenar los registros convertidos
    columnNames = [column[0] for column in cursor.description]  #
    for record in myresult:
        # Crear un diccionario que mapea los nombres de columna a los valores de registro
        insertObject.append(dict(zip(columnNames, record)))

    # Cerrar el cursor y devolver una plantilla HTML
    cursor.close()
    if insertObject == []:
        res = make_response("No se encontró ese producto", 404)
    else: res = make_response(insertObject,200)

    return res
   
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Ruta para guardar usuarios en la base de datos   se agrega aqui no?, como? , en la url?  osea en este archivo

# es que, aqui hacemos la inserción en la tabla de producto y la de imagen,   esto fue lo que copie para la otra inserción
# si, adaptar lo que tenemos aquí  en la carpeta de front
@product.post('/addProduct') 
def addProduct():
    new_product = request.get_json()
    id_user = new_product['id_user']
    titulo = new_product['titulo']
    descripcion = new_product['descripcion']
    existencia = new_product['existencia']
    precio = new_product['precio']
    categoria = new_product['categoria']
    imagen = new_product['imagen']


    if id_user and titulo and descripcion and existencia and precio and categoria and imagen:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO productos (id_user, titulo, descripcion, existencia, precio, categoria) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (id_user,titulo,descripcion,existencia, precio, categoria)
        cursor.execute(sql, data)
        db.database.commit()

        # Obtener el último ID insertado
        last_insert_id = cursor.lastrowid

        # Insertar en otra tabla utilizando el último ID
        cursor = db.database.cursor()
        sql = "INSERT INTO `imagenes` (`id_prod`, `imagen`) VALUES (%s, %s)"
        data = (last_insert_id, imagen)
        cursor.execute(sql, data)
        db.database.commit()

        return jsonify({'mensaje':'Producto registrado con exito'})
     except Exception as ex:
            return jsonify({'mensaje': "Error"})
     


@product.post("/addProductCar/<string:id>/<string:id_user>")
def addProductCar(id, id_user):
    try:
        cursor = db.database.cursor()
        cursor.execute("SELECT c.id FROM carrito c, usuario u, rel_user_car ruc WHERE c.vendido = 'no' AND ruc.id_car = c.id AND c.id = %s AND ruc.id_user = u.id AND u.id = %s", (id,id_user))
        result = cursor.fetchone()

        cursor = db.database.cursor()
        sql = "INSERT INTO `rel_car_prod` (`id_prod`, `id_car`) VALUES (%s, %s)"
        data = (id, result[0])  # Extraer el valor de la tupla
        cursor.execute(sql, data)
        db.database.commit()

        return jsonify({'mensaje': 'Producto registrado con éxito'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})



@product.delete('/deleteProd/<string:id>')
def deleteProd(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM productos WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El producto se ha eliminado correctamente"



@product.put('/editProd/<string:id>')
def editProd(id):
    update_product = request.get_json()
    titulo = update_product['titulo']
    descripcion = update_product['descripcion']
    existencia = update_product['existencia']
    precio = update_product['precio']
    categoria = update_product['categoria']

    if titulo and descripcion and existencia and precio and categoria:
       try:
        cursor = db.database.cursor()
        sql = "UPDATE productos SET  titulo = %s, descripcion = %s, existencia = %s, precio = %s, categoria = %s WHERE id = %s"
        data = (titulo, descripcion, existencia, precio, categoria, id)
        cursor.execute(sql, data)
        db.database.commit()
        
        return jsonify(data)
       except Exception as ex:
            return jsonify({'mensaje': "Error"})


##### Crud de aviso ######

#id del usuario
@product.get('/getNotice/<id>')
def getNotice(id):
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor() 

    cursor.execute("select a.*, u.nombre_usuario, p.titulo from usuario u, avisos a, productos p where a.id_user = u.id and a.id_prod = p.id and p.id_user = %s"%(str(id),))
   
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
                                              
#	id	id_prod	id_user	aviso	fecha 
@product.post('/addNotice/<string:id_prod>/<string:id_user>')
def addNotice(id_prod, id_user):
    new_notice = request.get_json()
    aviso = new_notice['aviso']

    if aviso:
        try:
            cursor = db.database.cursor()
            sql = "INSERT INTO avisos (id_prod, id_user, aviso) VALUES (%s, %s, %s)"
            data = (id_prod, id_user, aviso)
            cursor.execute(sql, data)
            db.database.commit()

            return jsonify({'mensaje': 'Aviso registrado con éxito'})
        except Exception as ex:
            return jsonify({'mensaje': 'Error'})


#id del aviso
@product.put("/updateNotice/<string:id>")
def updateNotice(id):
    update_notice = request.get_json()

    aviso = update_notice['aviso']

    if aviso: 

        cursor = db.database.cursor()
        
        sql = "UPDATE avisos SET aviso = %s, fecha = CURRENT_TIMESTAMP WHERE avisos.id = %s" 
        data = (aviso, id) 
        cursor.execute(sql, data)
        db.database.commit()
        resp = make_response(jsonify(data), 200)
    else:
        resp = make_response('Algo salió mal, revisa los datos...', 400)

    return resp


@product.delete("/deleteNotice/<string:id>")
def deleteNotice(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM avisos WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return "El aviso se ha eliminado correctamente"     
