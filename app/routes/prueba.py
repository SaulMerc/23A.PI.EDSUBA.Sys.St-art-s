from flask import Flask, request, redirect, Blueprint, url_for, send_from_directory, Blueprint, jsonify
from werkzeug.utils import secure_filename
import database as db
import os

app = Flask(__name__)
prueba = Blueprint('prueba', __name__, url_prefix='/api')
    # se obtene la ruta del proyecto mas la ruta de la carpeta 

                               
UPLOAD_FOLDER = os.path.abspath("./app/routes/uploads/")# este es el directorio donde vamos a guardar nuestras imagenes
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
prueba.config = app.config  # Asignar la configuración de la aplicación al blueprint



    # @prueba.route("/upload", methods=["GET", "POST"])
    # def upload_file():
    #     if request.method == "POST":
    #         if "file" not in request.files:
    #             return "No file part in the form."
            
    #         f = request.files["file"]
    #         if f.filename == "":
    #             return "No file selected."
            
    #         if f and allowed_file(f.filename):
    #             filename = secure_filename(f.filename) 
    #             f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

                
    #             id = request.form.get("id")
    #             titulo = request.form.get("titulo")
    #             descripcion = request.form.get("descripcion")
    #             existencia = request.form.get("existencia")
    #             precio = request.form.get("precio")
    #             categoria = request.form.get("categoria")
        
    #             print(id, titulo, descripcion, existencia, precio, categoria)

    #             cursor = db.database.cursor()
    #             sql = f"INSERT INTO productos (id, titulo, descripcion, existencia, precio, categoria) VALUES ('{id}', '{titulo}', '{descripcion}', '{existencia}', '{precio}', '{categoria}')"
    #             cursor.execute(sql) 
    #             db.database.commit()

    #             # Obtener el último ID insertado
    #             last_insert_id = cursor.lastrowid


    #             # Insertar en otra tabla utilizando el último ID
    #             cursor = db.database.cursor()
    #             sql = "INSERT INTO `imagenes` (`id_prod`, `imagen`) VALUES (%s, %s)"
    #             data = (last_insert_id, filename) 
    #             cursor.execute(sql, data)
    #             db.database.commit()


                
    #             return redirect(url_for("prueba.get_file", filename=filename))
            
    #         return "File not allowed."

    #     return """<!DOCTYPE html>
    # <html>
    # <head>
    #     <meta charset="utf-8">
    #     <title>Upload File</title>
    # </head>
    # <body>
    #     <h1>Upload File</h1>
    #     <form method="POST" enctype="multipart/form-data">
    #         <input type="file" name="file">
    #         <br><br>
    #         <label for="id">User ID:</label>
    #         <input type="text" name="id">
    #         <br><br>
    #         <label for="titulo">Title:</label>
    #         <input type="text" name="titulo">
    #         <br><br>
    #         <label for="descripcion">Description:</label>
    #         <input type="text" name="descripcion">
    #         <br><br>
    #         <label for="existencia">Stock:</label>
    #         <input type="text" name="existencia">
    #         <br><br>
    #         <label for="precio">Price:</label>
    #         <input type="text" name="precio">
    #         <br><br>
    #         <label for="categoria">Category:</label>
    #         <input type="text" name="categoria"> 
    #         <br><br>
    #         <input type="submit" value="Upload">
    #     </form>
    # </body>
    # </html>"""


###################################################################

@prueba.route("/upload/<string:id>", methods=["GET", "POST"])
def upload_file(id):
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in the form."
        
        f = request.files["file"]
        if f.filename == "":
            return "No file selected."
        
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename) 
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # id = request.form.get("id")
            titulo = request.form.get("titulo")
            descripcion = request.form.get("descripcion")
            existencia = request.form.get("existencia")
            precio = request.form.get("precio")
            categoria = request.form.get("categoria")

            print(id, titulo, descripcion, existencia, precio, categoria)

            cursor = db.database.cursor()
            sql = f"INSERT INTO productos (id_user, titulo, descripcion, existencia, precio, categoria) VALUES ('{id}', '{titulo}', '{descripcion}', '{existencia}', '{precio}', '{categoria}')"
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
            
            return jsonify({'mensaje': "El producto se agrego"})
            # return redirect(url_for("prueba.get_file", filename=filename))
           
        return "File not allowed."

    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Estilos CSS */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #2D3E40;
        }
        
        .header {
         
            background-color: #387373;
            color: #fff;
            padding: 20px;
        }
        
        .header h1 {
            margin: 0;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #93BFB7;
            color: #2D3E40;
            border-radius: 5px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        input[type="text"],
        input[type="number"],
        textarea {
            width: 98%;
            padding: 8px;
            border: 1px solid #97A6A0;
            border-radius: 5px;
            font-size: 14px;
        }
        
        input[type="file"] {
            display: none;
        }
        
        .file-label {
            display: inline-block;
            padding: 10px 20px;
            background-color: #387373;
            color: #fff;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .file-label:hover {
            background-color: #93BFB7;
        }
        
        .submit-btn {
            padding: 10px 20px;
            background-color: #2D3E40;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .submit-btn:hover {
            background-color: #97A6A0;
        }
        
        .footer {
            background-color: #E4F2E7;
            color: #2D3E40;
            padding: 20px;
            text-align: center;
        }
        
        /* Agrega más estilos según necesites */
    </style>
    <title>Editar Producto</title>
</head>
<body>
    <div class="header">
        <h1>starts</h1>
    </div>
    <div class="container">
        <h1>Agregar producto</h1>
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label for="file">Foto del Producto</label>
                <input type="file" name="file" id="file" required>
                <label for="file" class="file-label">Seleccionar archivo</label>
            </div>
            <div class="form-group">
                <label for="titulo">Título de la obra</label>
                <input type="text" name="titulo" id="titulo" placeholder="" required>
            </div>
            <div class="form-group">
                <label for="descripcion">Descripción</label>
                <textarea name="descripcion" id="descripcion" rows="3" placeholder="Ingresa una descripción" required></textarea>
            </div>
            <div class="form-group">
                <label for="existencia">Stock</label>
                <input type="number" name="existencia" id="existencia" required>
            </div>
            <div class="form-group">
                <label for="precio">Precio</label>
                <input type="number" name="precio" id="precio" placeholder="$$$" required>
            </div>
            <div class="form-group">
                <label for="categoria">Categoría</label>
                <input type="text" name="categoria" id="categoria" required>
            </div>
            <input type="submit" value="Guardar" class="submit-btn">
        </form>
    </div>
    <div class="footer">
        <p>Footer</p>
    </div>
</body>
</html>

    """



@prueba.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
