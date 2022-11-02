from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Course import Model_Course, Schema_Course

#Este metodo permite crear un curso
@app.route('/Course/Create', methods = ["POST"])
def create_Course():
	json = request.get_json(force=True)
	Course = Schema_Course().load(json)
	db.session.add(Course)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todas los cursos
@app.route('/Course', methods = ["GET"])
def all_Course():
	Course = Model_Course.query.all()
	json = Schema_Course(many = True).dump(Course)
	return jsonify(json), 200

#Este metodo permite buscar un curso mediante su id
@app.route('/Course/Search/id/<course_id>', methods = ["GET"])
def search_Course_id(course_id):
	Course = Model_Course.query.get(course_id)
	json = Schema_Course().dump(Course)
	return jsonify(json), 200

#Este metodo permite buscar un grado por su nombre
@app.route('/Course/Search/name_course/<name_course>', methods = ["GET"])
def search_Course_name_course(name_course):
	Courses = Model_Grade.query.filter(Model_Course.name_course.ilike(f'%{name_course}%')).all()
	json = Schema_Course(many = True).dump(Corses)
	return jsonify(json), 200


#Este metodo permite actualizar un curso
@app.route('/Course/Update', methods = ["PUT"])
def update_Course():
	json = request.get_json(force=True)
	Course = Model_Course.query.get(json['id'])
	if json['name_course']		!= '': Course.name_Course 		= json['name_Course']
	if json['describe']			!= '': Course.describe 			= json['describe']
	if json['picture_course']	!= '': Course.picture_course 	= json['picture_course']
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar un curso
@app.route('/Course/Delete/<Course_id>', methods = ["DELETE"])
def delete_Course(Course_id):
	Course = Model_Course.query.get(Course_id)
	db.session.delete(Course)
	db.session.commit()
	return "OK", 200

#Este metodo permite activar y desctivar un curso
@app.route('/Course/Update/is_activate/<course_id>', methods = ["PUT"])
def update_Course_is_activate(course_id):
	Course = Model_Course.query.get(course_id)
	if Course is None:
		return "The course does not exist", 204
	else:
		Course.is_activate = not Course.is_activate
		db.session.commit()
		return "The course was update", 200