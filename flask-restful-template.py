from flask import Flask, redirect, render_template, jsonify, url_for  # Importing Flask & Components
from flask_restful import Resource, Api  # Importing RESTFUL
from flask_cors import CORS  # Importing CORS

app = Flask(__name__)  # Declaring a new FLASK app
api = Api(app)  # Initializing Restful API
cors = CORS(app)  # Initializing Cross-Origin Resource Sharing


class EchoTest(Resource):  # returns an echo
    def get(self):  # GET METHOD function
        _str = {'type': 'GET', 'content': 'hello!'}  # json reply string
        return jsonify(_str)  # returning jsonified reply str


api.add_resource(EchoTest, '/echo')  # Echo test


if __name__ == "__main__":
    app.run()  # run Flask app


# temlpate by Teddy Morduhovich.
# requirements:
# pip install flask
# pip install flask_restful
# pip install flask_cors
# Python 3.x
