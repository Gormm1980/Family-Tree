"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, GrandParents, Parents, Children, Select_family
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route("/grandparents",methods=['GET'])
def all_grandpa():
    grandparents = GrandParents.get_all()
    grandpa_Dic = []
    for person in grandparents :
       grandpa_Dic.append(person.serialize())
    return jsonify(grandpa_Dic)

@app.route("/grandparents/<int:grandparents_id>",methods=['GET'])
def get_one_grandpa(grandparents_id):
    grandparents = GrandParents.get_one(grandparents_id)
    grandparents_serialized = grandparents.serialized()
    return jsonify(grandparents_serialized)

@app.route("/parents",methods=['GET'])
def all_parents():
    parents = Parents.get_all()
    parents_Dic = []
    for person in parents :
       parents_Dic.append(person.serialize())
    return jsonify(parents_Dic)

@app.route("/parents/<int:parents_id>",methods=['GET'])
def get_one_parent(parents_id):
    parents = Parents.get_one(parents_id)
    parents_serialized = parents.serialized()
    return jsonify(parents_serialized)

@app.route("/children",methods=['GET'])
def all_children():
    children = Children.get_all()
    children_Dic = []
    for person in children :
       children_Dic.append(person.serialize())
    return jsonify(children_Dic)

@app.route("/children/<int:children_id>",methods=['GET'])
def get_one_children(children_id):
    children = Children.get_one(children_id)
    children_serialized = children.serialized()
    return jsonify(children_serialized)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
