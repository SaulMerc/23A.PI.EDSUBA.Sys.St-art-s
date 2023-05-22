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

            
#             id_user = request.form.get("id_user")
#             titulo = request.form.get("titulo")
#             descripcion = request.form.get("descripcion")
#             existencia = request.form.get("existencia")
#             precio = request.form.get("precio")
#             categoria = request.form.get("categoria")
    
#             print(id_user, titulo, descripcion, existencia, precio, categoria)

#             cursor = db.database.cursor()
#             sql = f"INSERT INTO productos (id_user, titulo, descripcion, existencia, precio, categoria) VALUES ('{id_user}', '{titulo}', '{descripcion}', '{existencia}', '{precio}', '{categoria}')"
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
#         <label for="id_user">User ID:</label>
#         <input type="text" name="id_user">
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
#         <input type="text" name="categoria"> le vas a preguntar a gpt?
#         <br><br>
#         <input type="submit" value="Upload">
#     </form>
# </body>
# </html>"""


###################################################################

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
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/style.css">
    <title>Editar Producto</title>
</head>

<body class="gridMain">
    <header class="gridH ">
        <nav class="navP bcCom cComp">
            <div class="menu flexC">
                <button type="button" class="unset">
                    <img src="" type="image/svg+xml" class="imgM" alt="">
                </button>
            </div>

            <div class="logo flexC">
                <a href="../../index.html"><img class="imageLogo" alt=""></a>
            </div>
            <div class="search flexC">
                <input type="text" class="navB" placeholder="Pinturas de..." onkeypress="buscar">
                <button type="button" class="searchBtn" onclick="">
                    Buscar
                </button>
            </div>
            <div class="login flexC">
                <a href="signIn.html">Iniciar sesión</a>&nbsp;&nbsp;<a href="signUp.html">
                    Registrarse</a>
            </div>
            <div class="cart flexC">
                <a href="cart.html"><img src="" alt="" class="imageCart"></a>
            </div>
        </nav>
        <div class="sidebar bcCom">
            <h2 class="cWhite">Categorias</h2><br>
            <ul>
                <li><a href="search.html">Opción 1</a></li>
                <li><a href="search.html">Opción 2</a></li>
                <li><a href="search.html">Opción 3</a></li>
            </ul><br>
            <h2 class="cWhite">Modo oscuro</h2>
            <label class="switch">
                <input type="checkbox" id="dark__ModeToggle">
                <span class="slider round"></span>
            </label>
        </div>
    </header>
    <main class="gridM iFlex">

        <section class="cardDef bcWhite">


        
            <form action="POST">

                <div class="gridSProd">

                    <div class="gridCat flexCL padd20 img__cardG">
                        <label for="Cat">Categoria<i>*</i></label>
                        <select name="Cat" id="">
                            <option value="" disabled>Elige una opción</option>
                        </select><br>
                    </div>

                    <div class="gridImg  flexC padd10 ">
                        <label for="id_user">Foto del Producto<i>*</i></label>
                        <input type="number" name="id_user" id=""><br>
                        <hr>
                    </div>

                    <div class="gridImg  flexC padd10 ">
                        <label for="file">Foto del Producto<i>*</i></label>
                        <input type="file" name="file" id=""><br>
                        <hr>
                    </div>
                    <div class="gridTitl flexCL padd20">
                        <label for="titulo">Titulo de la obra<i>*</i></label>
                        <input type="text" name="titulo" id="" placeholder="Nombre..."><br>
                    </div>
                    <div class="gridDesc padd20">
                        <label for="descripcion">Descripción<i>*</i></label>
                        <textarea name="descripcion" id="" rows="3" cols="70" placeholder="Ingresa un descripción"></textarea><br>
                    </div>
                    <div class="gridPrice flexCL padd20">
                        <label for="precio">Precio<i>*</i></label>
                        <input type="number" name="precio" id="" placeholder="$$$"><br>
                    </div>
                    <input type="submit" value="Guardar">
                    
                    <div class="gridAvalia flexCL padd5">
                    </div>

                    <div class="gridBtc padd20 flexC">
                        <input type="button" value="Añadir al carrito" class="btnCart padd10" disabled>
                    </div>
                    <div class="gridComTitl flexCL padd20">
                        <h3>Comentarios</h3>
                    </div>
                    <div class="gridInsCom padd20 flexCL">
                        <input type="text" value="" class="btnCart padd10 margR5" placeholder="Comentario ..." disabled>
                        <input type="button" value="Comentar" class="btnCom" disabled> 
                    </div>
                    <div class="gridCom flexCL padd20">
                        <h3>-Esta es una visualización de como se vería acomodada la información de tu obre tu obra-</h3>
                    </div>
                    <div class="gridDate flexCL padd20">
                        <label for="FechaCreacion">Fecha de elaboración <i>*</i> </label><br>
                        <input type="date" name="FechaCreacion" id=""><br>
                    </div>
                </div>
            </form>
        </section>
    </main>
    <footer class="gridF">
        Footer no
    </footer>
    <script src="../scripts/script.js"></script>
</body>

</html>"""

@prueba.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
