from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_User import Model_User, Schema_User

# Este metodo permite crear un usuario
@app.route('/User/Create', methods = ["POST"])
def create_User():
	json = request.get_json(force=True)
	print(json)
	json['type_document'] = json['type_document'].upper()
	print(json)
	User = Schema_User().load(json)
	db.session.add(User)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todos los usuarios
@app.route('/User', methods = ["GET"])
def all_Users():
	Users = Model_User.query.all()
	json = Schema_User(many = True).dump(Users)
	return jsonify(json), 200
	
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
	User = Model_User.query.get(json['id'])
	if json['name'] 			!= '': User.name 			= json['name']
	if json['last_name_1'] 		!= '': User.last_name_1 	= json['last_name_1']
	if json['last_name_2'] 		!= '': User.last_name_2 	= json['last_name_2']
	if json['type_document'] 	!= '': User.type_document 	= json['type_document']
	if json['document'] 		!= '': User.document 		= json['document']
	if json['describe'] 		!= '': User.describe 		= json['describe']
	if json['picture'] 			!= '': User.picture 		= json['picture']
	if json['password'] 		!= '': User.password 		= json['password']
	db.session.commit()
	return "OK", 200

#Este metodo permite actualizar la contrasena
@app.route('/User/Update/password', methods = ["PUT"])
def update_User_password():
	json = request.get_json(force=True)
	id = json['id']
	document = json['document']
	password = json['password']
	User = Model_User.query.get(id)
	if User.username == username and User.password != password: User.password = password
	return "OK", 200

#Este metodo permite eliminar un usuario
@app.route('/User/Delete/<user_id>', methods = ["DELETE"])
def delete_User(user_id):
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
		Model_Users.document, 
		Model_Users.admin,
		Model_Users.is_activate
	).all()
	json = Schema_User(many = True).dump(Users)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

# Metodo que permite contar la cantidad de usuarios de la plataforma
@app.route('/User/Amount', methods = ["GET"])
def totalUsers():
	Users = Model_Users.query.with_entities(
		Model_Users.id,
	).all()
	print(len(Users))
	response = jsonify(total = len(Users))
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

#Este metodo permite activar y desctivar un usuario
@app.route('/User/Update/is_activate/<user_id>', methods = ["PUT"])
def update_User_is_activate(user_id):
	User = Model_User.query.get(user_id)
	if User is None: 
		return "The user does not exist", 204
	else: 
		User.is_activate = not User.is_activate
		db.session.commit()
		return "The user was update", 200