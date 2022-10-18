from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Grade import Model_Grade, Schema_Grade

#Este metodo permite crear un grado
@app.route('/Grade/Create', methods = ["POST"])
def create_Grade():
	json = request.get_json(force=True)
	Grade = Schema_Grade().load(json)
	db.session.add(Grade)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todos los usuarios
@app.route('/Grade', methods = ["GET"])
def all_Grades():
	Grades = Model_Grade.query.all()
	json = Schema_Grade(many = True).dump(Grades)
	return jsonify(json), 200

#Este metodo permite buscar un grado mediante su id
@app.route('/Grade/Search/id/<grade_id>', methods = ["GET"])
def search_Grade_id(grade_id):
	Grade = Model_Grade.query.get(grade_id)
	json = Schema_Grade().dump(Grade)
	return jsonify(json), 200

#Este metodo permite actualizar un grado
@app.route('/Grade/Update', methods = ["PUT"])
def update_Grade():
	json = request.get_json(force=True)
	id = json['id']
	name_grade = json['name_grade']
	describe = json['describe']

	Grade = Model_Grade.query.get(id)

	if name_grade != '': Grade.name_grade = name_grade
	if describe != '': Grade.describe = describe
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar un grado
@app.route('/Grade/Delete/<grade_id>', methods = ["DELETE"])
def delte_Grade(grade_id):
	Grade = Model_Grade.query.get(grade_id)
	db.session.delete(Grade)
	db.session.commit()
	return "OK", 200