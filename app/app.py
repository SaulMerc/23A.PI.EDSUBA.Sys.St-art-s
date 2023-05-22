from flask import Flask, Blueprint, render_template, request
from routes.user import user
# from routes.images import images
from routes.comment import comment
from routes.car import car
from routes.product import product
from routes.category import category
from routes.rol import rol
from flask_cors import CORS
import mysql.connector
from uuid import uuid4
import os
from database import database as db

app=Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "http://34.208.161.62/"}})#UrlProduccion
CORS(app) #URL dev
app.register_blueprint(user)
# app.register_blueprint(images)
app.register_blueprint(comment)
app.register_blueprint(car)
app.register_blueprint(product)
app.register_blueprint(category)
app.register_blueprint(rol)


@app.route("/")
def raiz():
    
    return render_template("index.html")

@app.route("/cart/")
def singIn():

    return render_template("cart.html")

@app.route("/addProduct", methods =['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        id_user = request.form['id_user']
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        existencia = request.form['existencia']
        precio = request.form['precio']
        categoria = request.form['categoria']
        
        # Obtener el archivo de imagen subido
        imagen = request.files['imagen']
        
        # Guardar la imagen en una carpeta en el servidor
        imagen.save('ruta/a/la/carpeta/' + imagen.filename)
        
        # Realizar el procesamiento adicional con los datos y la imagen
        
        return 'Formulario enviado correctamente'
    return render_template('formulario.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

