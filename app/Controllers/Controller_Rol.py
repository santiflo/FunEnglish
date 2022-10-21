from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Rol import Model_Rol, Schema_Rol

#Este metodo permite crear un rol
@app.route('/Rol/Create', methods = ['POST'])
def create_Rol():
	json = request.get_json(force=True)
	Rol = Schema_Rol().load(request.get_json())
	db.session.add(Rol)
	db.session.commit()
	return "Rol creado", 201

#Este metodo permite listar todos los roles
@app.route('/Rol', methods = ['GET'])
def all_Rol():
	Rols = Model_Rol.query.all()
	json = Schema_Rol(many=True).dump(Rols)
	return jsonify(json), 200

#Este metodo permite actualizar un rol
@app.route('/Rol/Update', methods=['PUT'])
def update_Rol():
	json = request.get_json(force=True)
	Rol = Model_Rol.query.get(json['id'])
	if json['name_rol'] != '': Rol.name_rol = json['name_rol']
	if json['describe'] != '': Rol.describe = json['describe']
	db.session.commit()
	return "Rol updated", 200

#Este metodo permite eliminar un rol
@app.route('/Rol/Delete/<rol_id>', methods = ['DELETE'])
def delete_rol(rol_id):
	Rol = Model_Rol.query.get(rol_id)
	db.session.delete(Rol)
	db.session.commit()
	return "OK", 200