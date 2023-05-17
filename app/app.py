from flask import Flask, Blueprint
from routes.user import user
from routes.images import images

app=Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(images)



if __name__=='__main__':
    app.run(debug=True,port=3000)