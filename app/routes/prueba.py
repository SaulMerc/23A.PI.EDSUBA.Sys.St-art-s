from flask import Flask, request, redirect, Blueprint, url_for, send_from_directory, Blueprint
from werkzeug.utils import secure_filename
import database as db
import os

app = Flask(__name__)
prueba = Blueprint('prueba', __name__, url_prefix='/api')
    # se obtene la ruta del proyecto mas la ruta de la carpeta 

                               
UPLOAD_FOLDER = os.path.abspath("./routes/uploads/")# este es el directorio donde vamos a guardar nuestras imagenes
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
prueba.config = app.config  # Asignar la configuración de la aplicación al blueprint

@prueba.route('/h')
def hello():
    print(UPLOAD_FOLDER)
    return 'Hello World!'


@prueba.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in the form."
        
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename) 
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            
            id_user = request.form.get("id_user")
            titulo = request.form.get("titulo")
            descripcion = request.form.get("descripcion")
            existencia = request.form.get("existencia")
            precio = request.form.get("precio")
            categoria = request.form.get("categoria")
    
            print(id_user, titulo, descripcion, existencia, precio, categoria)

            cursor = db.database.cursor()
            sql = f"INSERT INTO productos (id_user, titulo, descripcion, existencia, precio, categoria) VALUES ('{id_user}', '{titulo}', '{descripcion}', '{existencia}', '{precio}', '{categoria}')"
            cursor.execute(sql) 
            db.database.commit()

            # Obtener el último ID insertado
            last_insert_id = cursor.lastrowid


            # Insertar en otra tabla utilizando el último ID
            cursor = db.database.cursor()
            sql = "INSERT INTO `imagenes` (`id_prod`, `imagen`) VALUES (%s, %s)"
            data = (last_insert_id, filename) 
            cursor.execute(sql, data)
            db.database.commit()


            
            return redirect(url_for("prueba.get_file", filename=filename))
        
        return "File not allowed."

    return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Upload File</title>
</head>
<body>
    <h1>Upload File</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <br><br>
        <label for="id_user">User ID:</label>
        <input type="text" name="id_user">
        <br><br>
        <label for="titulo">Title:</label>
        <input type="text" name="titulo">
        <br><br>
        <label for="descripcion">Description:</label>
        <input type="text" name="descripcion">
        <br><br>
        <label for="existencia">Stock:</label>
        <input type="text" name="existencia">
        <br><br>
        <label for="precio">Price:</label>
        <input type="text" name="precio">
        <br><br>
        <label for="categoria">Category:</label>
        <input type="text" name="categoria"> le vas a preguntar a gpt?
        <br><br>
        <input type="submit" value="Upload">
    </form>
</body>
</html>"""

@prueba.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
