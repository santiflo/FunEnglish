from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_User import Model_User, Schema_User

#Este metodo permite crear un usuario
@app.route('/User/Create', methods = ["POST"])
def create_User():
	json = request.get_json(force=True)
	print(json)
	json['type_document'] = json['type_document'].upper()
	print(json)
	User = Schema_User().load(request.get_json())
	db.session.add(User)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todos los usuarios
@app.route('/User', methods = ["GET"])
def all_Users():
	Users = Model_User.query.all()
	json = Schema_User(many = True).dump(Users)
	return jsonify(json), 200

"""
@app.route('/User', methods = ["GET"])
def search_User_name(user_name):
	Users = Model_Users.query.filter(Model_Users.username.ilike('%'+user_name+'%')).all()
	json = Schema_Users(many = True).dump(Users)
	return jsonify(json), 200
"""

#Este metodo permite buscar un usuario mediante su id
@app.route('/User/Search/id/<user_id>', methods = ["GET"])
def search_User_id(user_id):
	User = Model_User.query.get(user_id)
	json = Schema_User().dump(User)
	return jsonify(json), 200

#Este metodo permite actualizar un usuario
@app.route('/User/Update', methods = ["PUT"])
def update_User():
	json = request.get_json(force=True)
	id = json['id']
	name = json['name']
	last_name_1 = json['last_name_1']
	last_name_2 = json['last_name_2']
	type_document = json['type_document']
	document = json['document']
	describe = json['describe']
	picture = json['picture']

	User = Model_User.query.get(id)

	if name != '': User.name = name
	if last_name_1 != '': User.last_name_1 = last_name_1
	if last_name_2 != '': User.last_name_2 = last_name_2
	if type_document != '': User.type_document = type_document
	if document != '': User.document = document
	if describe != '': User.describe = describe
	if picture != '': User.picture = picture
	db.session.commit()
	return "OK", 200

#Este metodo permite actualizar la contrasena
@app.route('/User/Update/password', methods = ["PUT"])
def update_User_password():
	json = request.get_json()
	id = json['id']
	document = json['document']
	password = json['password']
	User = Model_User.query.get(id)
	if User.username == username and User.password != password: User.password = password
	return "OK", 200

#Este metodo permite eliminar un usuario
@app.route('/User/Delete/<user_id>', methods = ["DELETE"])
def delte_User(user_id):
	User = Model_User.query.get(user_id)
	db.session.delete(User)
	db.session.commit()
	return "OK", 200

#Este metodo permite traer la informacion del usuario para desplegar en el menu
@app.route('/User/Menu/<user_id>', methods = ["GET"])
def menu_User(user_id):
	User = Model_User.query.get(user_id)
	if User is None:
		return "El usuario no existe", 204
	else:
		response = jsonify(
			name = User.name,
			picture = User.picture)
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response, 200

#Este metodo permite traer unos campos especificos para el administrador
@app.route('/User/Administrator', methods = ["GET"])
def adminUsers():
	Users = Model_User.query.with_entities(
		Model_Users.id, 
		Model_Users.name, 
		Model_Users.email, 
		Model_Users.admin,
		Model_Users.req_admin
	).all()
	json = Schema_User(many = True).dump(Users)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

@app.route('/User/Amount', methods = ["GET"])
def TotalUsers():
	Users = Model_Users.query.with_entities(
		Model_Users.id,
	).all()
	print(len(Users))
	response = jsonify(total = len(Users))
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

"""
@app.route('/Users/Uptdate/Rol', methods = ["PUT"])
def UpdateAdmin():
	json = request.get_json(force=True)
	print(json)
	print(json["id"])
	id = json["id"]
	User = Model_Users.query.get(int(json["id"]))

	if User is None:
		return "El usuario no existe", 204
	elif User.admin == 0:
		User.admin = 1
		User.req_admin = 0
	elif User.admin == 1:
		User.admin = 0
	db.session.commit()
	return "OK", 200
"""