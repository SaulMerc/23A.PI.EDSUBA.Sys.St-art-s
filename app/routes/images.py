from flask import Flask, Blueprint, jsonify, request, make_response

import database as db

images = Blueprint('images', __name__,url_prefix='/api')

@images.route('/upload/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    file_path = '/home/waldo/fotos-perfil/' + uploaded_file.filename
    uploaded_file.save(file_path)
    
    
    cursor = db.database.cursor()
    
   
    query = "INSERT INTO `fotos_perfil` (`id`, `id_user`, `imagen`) VALUES (NULL, '2', %s)"
    values = (file_path,)
    cursor.execute(query, values)

    
    db.database.commit()
    cursor.close()
    
    return 'Archivo subido y ruta guardada en la base de datos.'



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