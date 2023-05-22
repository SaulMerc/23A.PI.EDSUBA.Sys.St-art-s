from flask import Flask, Blueprint, jsonify, request, make_response

import database as db

images = Blueprint('images', __name__,url_prefix='/api')

@images.route('/upload/<id>', methods=['POST'])
def upload_file(id):
    uploaded_file = request.files['file']
    file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
    uploaded_file.save(file_path)
    
    cursor = db.database.cursor()
                                                                        
    query = f"INSERT INTO `fotos_perfil` (`id`, `id_user`, `imagen`) VALUES (NULL, {id}, {file_path})"
    cursor.execute(query)
 
    db.database.commit()
    cursor.close()
    
    return 'Archivo subido y ruta guardada en la base de datos.'


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


@images.put('/editImage/<string:id>')
def editImage(id):
    update_image = request.get_json()
    imagen = update_image['imagen']
    if imagen:
        cursor = db.database.cursor()
        sql = "UPDATE fotos_perfil SET imagen = %s WHERE id = %s"
        data = (imagen, id)
        cursor.execute(sql, data)
        db.database.commit()
        resp=make_response(jsonify(data), 200)
    
    else: resp=make_response('Algo salio mal, revisa los datos...',400)

    return resp