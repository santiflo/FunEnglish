from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Class import Model_Class, Schema_Class

#Este metodo permite crear una clase
@app.route('/Class/Create', methods = ["POST"])
def create_Class():
	json = request.get_json(force=True)
	Class = Schema_Class().load(json)
	db.session.add(Class)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todas las clases
@app.route('/Class', methods = ["GET"])
def all_Class():
	Class = Model_Class.query.all()
	json = Schema_Class(many = True).dump(Class)
	return jsonify(json), 200

#Este metodo permite buscar una clase mediante su id
@app.route('/Class/Search/id/<class_id>', methods = ["GET"])
def search_Class_id(class_id):
	Class = Model_Class.query.get(class_id)
	json = Schema_Class().dump(Class)
	return jsonify(json), 200

#Este metodo permite actualizar una clase
@app.route('/Class/Update', methods = ["PUT"])
def update_Class():
	json = request.get_json(force=True)
	id = json['id']
	name_class = json['name_class']
	describe = json['describe']

	Class = Model_Class.query.get(id)

	if name_class != '': Class.name_class = name_class
	if describe != '': Class.describe = describe
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar un grado
@app.route('/Class/Delete/<class_id>', methods = ["DELETE"])
def delte_Grade(class_id):
	Class = Model_Class.query.get(class_id)
	db.session.delete(Class)
	db.session.commit()
	return "OK", 200