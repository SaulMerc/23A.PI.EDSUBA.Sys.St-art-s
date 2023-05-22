from flask import Flask, Blueprint
from routes.user import user
from routes.images import images
from routes.comment import comment
from routes.car import car
from routes.product import product
from routes.prueba import prueba


#registramos nuestros blueprints
app=Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(images)
app.register_blueprint(comment)
app.register_blueprint(car)
app.register_blueprint(product)
app.register_blueprint(prueba)



if __name__=='__main__':
    app.run(debug=True,port=3000)