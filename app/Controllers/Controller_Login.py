from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_User import Model_User, Schema_User

# Este metodo permite loguear un usuario
@app.route('/Login', methods = ["POST"])
def Login():
	json = request.get_json(force=True)
	print(json['document'],json['password'])
	User = Model_User.query.filter_by(document = json['document']).first()
	if User is None: 
		return "Bad user or password", 204
	elif User.password == json['password']:
		response = jsonify(
			id = User.id,
			rol_id = User.rol_id
			)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 202
	else: return "Bad user or password", 204
	#return "Bad user or password", 204