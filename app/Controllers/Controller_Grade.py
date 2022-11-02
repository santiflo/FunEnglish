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

#Este metodo permite listar todos los grados
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

#Este metodo permite buscar un grado por su nombre
@app.route('/Grade/Search/name_grade/<name_grade>', methods = ["GET"])
def search_Grade_name_grade(grade_name):
	Grades = Model_Grade.query.filter(Model_Grade.grade_name.ilike(f'%{name_grade}%')).all()
	json = Schema_Grade(many = True).dump(Grades)
	return jsonify(json), 200


#Este metodo permite actualizar un grado
@app.route('/Grade/Update', methods = ["PUT"])
def update_Grade():
	json = request.get_json(force=True)
	Grade = Model_Grade.query.get(json['id'])
	if json['name_grade'] != '': Grade.name_grade = json['name_grade']
	if json['describe'] != '': Grade.describe = json['describe']
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar un grado
@app.route('/Grade/Delete/<grade_id>', methods = ["DELETE"])
def delete_Grade(grade_id):
	Grade = Model_Grade.query.get(grade_id)
	db.session.delete(Grade)
	db.session.commit()
	return "OK", 200

#Este metodo permite activar y desctivar un grado
@app.route('/Grade/Update/is_activate/<grade_id>', methods = ["PUT"])
def update_Grade_is_activate(grade_id):
	Grade = Model_Lesson.query.get(grade_id)
	if Grade is None:
		return "The grade does not exist", 204
	else:
		Grade.is_activate = not Grade.is_activate
		db.session.commit()
		return "The grade was update", 200

"""
@app.route('/User', methods = ["GET"])
def search_User_name(user_name):
	Users = Model_Users.query.filter(Model_Users.username.ilike('%'+user_name+'%')).all()
	json = Schema_Users(many = True).dump(Users)
	return jsonify(json), 200
"""