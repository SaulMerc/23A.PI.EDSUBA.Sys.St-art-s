from flask import Flask, Blueprint, jsonify, request, make_response, url_for, send_from_directory
from werkzeug.utils import secure_filename
import database as db
import os

app = Flask(__name__)
images = Blueprint('images', __name__,url_prefix='/api')

# @images.route('/upload/', methods=['POST'])
# def upload_file():
#     uploaded_file = request.files['file']
#     file_path = '/home/waldo/fotos-perfil/' + uploaded_file.filename
#     uploaded_file.save(file_path)
    
    
#     cursor = db.database.cursor()
    
   
#     query = "INSERT INTO `fotos_perfil` (`id`, `id_user`, `imagen`) VALUES (NULL, '2', %s)"
#     values = (file_path,)
#     cursor.execute(query, values)

    
#     db.database.commit()
#     cursor.close()
    
#     return 'Archivo subido y ruta guardada en la base de datos.'



# <!DOCTYPE html>
# <html>
# <head>
#     <title>Subir archivo</title>
# </head>
# <body>
#     <form method="post" action="http://localhost:3000/upload/" enctype="multipart/form-data">
#         <input type="file" name="file">
#         <button type="submit">Subir archivo</button>
#     </form>
    
 
# </body>
# </html>



@images.route('/images/<user_id>', methods=['GET'])
def get_user_images(user_id):
   
    cursor = db.database.cursor()
    
   
    query = "SELECT `id`, `imagen` FROM `fotos_perfil` WHERE `id_user` = %s"
    values = (user_id,)
    cursor.execute(query, values)
    results = cursor.fetchall()
    
    cursor.close()
   
    if not results:
        return jsonify({'error': 'No se encontraron imágenes para el usuario dado.'}), 404
    
    # Construir una lista de imágenes con sus ID y rutas
    images = [{'id': row[0], 'image_path': row[1]} for row in results]
    
    # Construir el JSON de respuesta
    response = {
        'user_id': user_id,
        'images': images
    }
    
    return jsonify(response)

##################################################################
# "./routes/fotosPerfil/"
UPLOAD_FOLDER = os.path.abspath("./routes/fotosPerfil/")# este es el directorio donde vamos a guardar nuestras imagenes
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
images.config = app.config  # Asignar la configuración de la aplicación al blueprint




@images.route("/fotoPerfil", methods=["GET", "POST"])
def fotoPerfil():
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

            # Insertar en otra tabla utilizando el último ID   
            cursor = db.database.cursor()
            sql = "INSERT INTO `fotos_perfil` (`id_user`, `imagen`) VALUES (%s, %s)"
            data = (id_user, filename)
            cursor.execute(sql, data)
            db.database.commit()


            
            # return redirect(url_for("images.get_file", filename=filename))
            return "La foto de perfil se agrego con exito"
        
        return "File not allowed."

    return """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Upload File</title>
</head>
<body>
    <h1>Foto de perfil</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <br><br>
        <label for="id_user">User ID:</label>
        <input type="text" name="id_user">

        <br><br>
        <input type="submit" value="Upload">
    </form>
</body>
</html>"""