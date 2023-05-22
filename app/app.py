from flask import Flask, Blueprint, render_template
from routes.user import user
from routes.images import images
from routes.comment import comment
from routes.car import car
from routes.product import product
from routes.category import category
from routes.rol import rol
from flask_cors import CORS

app=Flask(__name__)
#CORS(app, resources={r"/*": {"origins": "http://34.208.161.62/"}})#UrlProduccion
CORS(app) #URL dev
app.register_blueprint(user)
app.register_blueprint(images)
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

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

