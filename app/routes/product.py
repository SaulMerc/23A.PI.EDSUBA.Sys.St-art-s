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

# Ruta para guardar usuariosen la base de datos
@product.post('/addProduct/')
def addProduct():
    id_user = request.form.get('id_user')
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    existencia = request.form.get('existencia')
    precio = request.form.get('precio')
    categoria = request.form.get('categoria')
    uploaded_file = request.files['file']


    if id_user and titulo and descripcion and existencia and precio and categoria:
     try:
        cursor = db.database.cursor()
        sql = "INSERT INTO productos (id_user, titulo, descripcion, existencia, precio, categoria) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (id_user,titulo,descripcion,existencia, precio, categoria)
        cursor.execute(sql, data)
        db.database.commit()

        # Obtener el último ID insertado
        last_insert_id = cursor.lastrowid

        # Insertar en otra tabla utilizando el último ID
        file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
        uploaded_file.save(file_path)
    
        cursor = db.database.cursor()
                                                                        
        query = f"INSERT INTO `imagenes` (`id`, `id_prod`, `imagen`) VALUES (NULL, {last_insert_id}, {file_path})"
        cursor.execute(query)
 
        db.database.commit()
        cursor.close()

        

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


