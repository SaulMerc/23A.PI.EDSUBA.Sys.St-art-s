# from flask import Flask, Blueprint, jsonify, request, make_response

# import database as db

# images = Blueprint('images', __name__,url_prefix='/api')

# @images.route('/uploadFp/<string:id>', methods=['POST'])
# def upload_fileFp(id):
#     uploaded_file = request.files['file']
#     file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
#     uploaded_file.save(file_path)
    
#     cursor = db.database.cursor()
                                                                        
#     query = f"INSERT INTO `fotos_perfil` (`id`, `id_user`, `imagen`) VALUES (NULL, {id}, {file_path})"
#     cursor.execute(query)
 
#     db.database.commit()
#     cursor.close()
    
#     return 'Archivo subido y ruta guardada en la base de datos.'


# @images.route('/imagesFp/<id>', methods=['GET'])
# def get_user_imagesFp(id):
   
#     cursor = db.database.cursor()
    
   
#     query = "SELECT `id`, `imagen` FROM `fotos_perfil` WHERE `id_user` = %s"
#     values = (id,)
#     cursor.execute(query, values)
#     results = cursor.fetchall()
    
#     cursor.close()
   
#     if not results:
#         return jsonify({'error': 'No se encontraron imágenes para el usuario dado.'}), 404
    
#     # Construir una lista de imágenes con sus ID y rutas
#     images = [{'id': row[0], 'image_path': row[1]} for row in results]
    
#     # Construir el JSON de respuesta
#     response = {
#         'user_id': id,
#         'images': images
#     }
    
#     return jsonify(response)


# @images.put('/editImageFp/<string:id>')
# def editImageFp(id):
#     uploaded_file = request.files['file']
#     file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
#     uploaded_file.save(file_path)
    
#     cursor = db.database.cursor()
#     if uploaded_file:
#         cursor = db.database.cursor()
#         sql = "UPDATE fotos_perfil SET imagen = %s WHERE id = %s"
#         data = (file_path, id)
#         cursor.execute(sql, data)
#         db.database.commit()
#         resp=make_response(jsonify(data), 200)
    
#     else: resp=make_response('Algo salio mal, revisa los datos...',400)

#     return resp

# @images.delete('/deleteImage/<string:id>')
# def deleteImageFp(id):
#     # Crea un objeto cursor para ejecutar comandos en la base de datos
#     cursor = db.database.cursor()
#     sql = "DELETE FROM fotos_perfil WHERE id=%s"
#     # Crea una tupla con el valor del parámetro id
#     data = (id,)
#     cursor.execute(sql, data)
#     db.database.commit()
#     return "La foto se ha eliminado correctamente"


#     ### Subir imagen de producto ###


# @images.route('/upload/<string:id>', methods=['POST'])
# def upload_fileFp(id):
#     uploaded_file = request.files['file']
#     file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
#     uploaded_file.save(file_path)
    
#     cursor = db.database.cursor()
                                                                        
#     query = f"INSERT INTO `imagenes` (`id`, `id_prod`, `imagen`) VALUES (NULL, {id}, {file_path})"
#     cursor.execute(query)
 
#     db.database.commit()
#     cursor.close()
    
#     return 'Archivo subido y ruta guardada en la base de datos.'


# @images.route('/images/<id>', methods=['GET'])
# def get_user_images(id):
   
#     cursor = db.database.cursor()
    
   
#     query = "SELECT `id`, `imagen` FROM `imagenes` WHERE `id_user` = %s"
#     values = (id,)
#     cursor.execute(query, values)
#     results = cursor.fetchall()
    
#     cursor.close()
   
#     if not results:
#         return jsonify({'error': 'No se encontraron imágenes para el usuario dado.'}), 404
    
#     # Construir una lista de imágenes con sus ID y rutas
#     images = [{'id': row[0], 'image_path': row[1]} for row in results]
    
#     # Construir el JSON de respuesta
#     response = {
#         'user_id': id,
#         'images': images
#     }
    
#     return jsonify(response)


# @images.put('/editImage/<string:id>')
# def editImage(id):
#     uploaded_file = request.files['file']
#     file_path = 'C:\\Users\\waldi\\Desktop\\PruebasSUBIDAIMAGENEDS\\' + uploaded_file.filename
#     uploaded_file.save(file_path)
    
#     cursor = db.database.cursor()
#     if uploaded_file:
#         cursor = db.database.cursor()
#         sql = "UPDATE imagenes SET imagen = %s WHERE id = %s"
#         data = (file_path, id)
#         cursor.execute(sql, data)
#         db.database.commit()
#         resp=make_response(jsonify(data), 200)
    
#     else: resp=make_response('Algo salio mal, revisa los datos...',400)

#     return resp

# @images.delete('/deleteImage/<string:id>')
# def deleteImageFp(id):
#     # Crea un objeto cursor para ejecutar comandos en la base de datos
#     cursor = db.database.cursor()
#     sql = "DELETE FROM imagen WHERE id=%s"
#     # Crea una tupla con el valor del parámetro id
#     data = (id,)
#     cursor.execute(sql, data)
#     db.database.commit()
#     return "La foto se ha eliminado correctamente"