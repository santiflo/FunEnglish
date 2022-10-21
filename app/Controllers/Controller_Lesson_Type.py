from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Lesson_Type import Model_Lesson_Type, Schema_Lesson_Type

#Este metodo permite crear un tipo de leccion
@app.route('/Lesson_Type/Create', methods = ["POST"])
def create_Lesson_Type():
	json = request.get_json(force=True)
	Lesson_Type = Schema_Lesson_Type().load(json)
	db.session.add(Lesson_Type)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todas los tipos de lecciones
@app.route('/Lesson_Type', methods = ["GET"])
def all_Lesson_Type():
	Lesson_Type = Model_Lesson_Type.query.all()
	json = Schema_Lesson_Type(many = True).dump(Lesson_Type)
	return jsonify(json), 200

#Este metodo permite buscar un tipo de leccion mediante su id
@app.route('/Lesson_Type/Search/id/<lesson_type_id>', methods = ["GET"])
def search_Lesson_Type_id(lesson_type_id):
	Lesson_Type = Model_Lesson_Type.query.get(lesson_type_id)
	json = Schema_Lesson_Type().dump(Lesson_Type)
	return jsonify(json), 200

#Este metodo permite actualizar una leccion
@app.route('/Lesson_Type/Update', methods = ["PUT"])
def update_Lesson_Type():
	json = request.get_json(force=True)
	Lesson_Type = Model_Lesson_Type.query.get(json['id'])
	if json['name']			!= '' : Lesson_Type.title		= json['title']
	if json['description']	!= '' : Lesson_Type.description	= json['description']
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar una leccion
@app.route('/Lesson_Type/Delete/<lesson_type_id>', methods = ["DELETE"])
def delete_Lesson_Type(lesson_type_id):
	Lesson_Type = Model_Lesson_Type.query.get(lesson_type_id)
	db.session.delete(Lesson_Type)
	db.session.commit()
	return "OK", 200