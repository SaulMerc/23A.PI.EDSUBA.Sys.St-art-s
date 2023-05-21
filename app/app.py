from flask import Flask, Blueprint, render_template
from routes.user import user
from routes.images import images
from routes.comment import comment
from routes.car import car
from routes.product import product
from flask_cors import CORS

app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://34.208.161.62"}})
app.register_blueprint(user)
app.register_blueprint(images)
app.register_blueprint(comment)
app.register_blueprint(car)
app.register_blueprint(product)


@app.route("/")
def raiz():
    
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)

