from flask import Flask, render_template, request, redirect, url_for, Blueprint,make_response
import os
import database as db




car = Blueprint('car', __name__,url_prefix='/api')

id_user = ""
# Rutas de la aplicación

@car.route('/')
@car.route('/<string:id>')
def home(id):
    global id_user
    id_user = id
    # Crear un cursor para la base de datos y ejecutar una consulta SQL
    cursor = db.database.cursor()
    cursor.execute("SELECT ruc.id_user, u.nombre, c.id, c.vendido, c.fecha_vendido, p.titulo, p.precio FROM usuario u, carrito c, productos p, rel_user_car ruc, rel_car_prod rcp WHERE ruc.id_car = c.id AND rcp.id_car = c.id AND rcp.id_prod = p.id AND ruc.id_user = u.id AND u.id = %s;",(id,))
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
    # return insertObject
    return render_template('car.html', data=insertObject)
    #return insertObject



@car.route('/addCar/<string:id>')
def addCar(id):
    if id:
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

    return render_template("user.html")


@car.route('/deleteCar/<string:id>')
def deleteCar(id):
    # Crea un objeto cursor para ejecutar comandos en la base de datos
    cursor = db.database.cursor()
    sql = "DELETE FROM carrito WHERE id=%s"
    # Crea una tupla con el valor del parámetro id
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('car.home'))



@car.route('/editCar/<string:id>', methods=['POST'])
def editCar(id):
    vendido = request.form['vendido']
    global id_user
    if vendido:
        cursor = db.database.cursor()
        sql = "UPDATE carrito SET vendido = %s WHERE id = %s"
        data = (vendido, id)
        cursor.execute(sql, data)
        db.database.commit()

    # Generar la URL con los parámetros deseados
    parameters = {'id': id_user}  # Ejemplo de parámetros
    url = url_for('car.home', **parameters)

    return redirect(url)