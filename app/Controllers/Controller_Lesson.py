from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Lesson import Model_Lesson, Schema_Lesson

#Este metodo permite crear una leccion
@app.route('/Lesson/Create', methods = ["POST"])
def create_Lesson():
	json = request.get_json(force=True)
	Lesson = Schema_Lesson().load(json)
	db.session.add(Lesson)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todas las lecciones
@app.route('/Lesson', methods = ["GET"])
def all_Lesson():
	Lesson = Model_Lesson.query.all()
	json = Schema_Lesson(many = True).dump(Lesson)
	return jsonify(json), 200

#Este metodo permite buscar una leccion mediante su id
@app.route('/Lesson/Search/id/<lesson_id>', methods = ["GET"])
def search_Lesson_id(lesson_id):
	Lesson = Model_Lesson.query.get(lesson_id)
	json = Schema_Lesson().dump(Lesson)
	return jsonify(json), 200

#Este metodo permite buscar una leccion por su tipo de leccion
@app.route('/Lesson/Search/lesson_type_id/<lesson_type_id>', methods = ["GET"])
def search_Lesson_lesson_type_id(lesson_type_id):
	Lesson = Model_Lesson.query.filter(Model_Lesson.lesson_type_id.ilike(lesson_type_id)).all()
	json = Schema_Lesson(many = True).dump(Lesson)
	return jsonify(json), 200


#Este metodo permite actualizar una leccion
@app.route('/Lesson/Update', methods = ["PUT"])
def update_Lesson():
	json = request.get_json(force=True)
	Lesson = Model_Lesson.query.get(json['id'])
	if json['title']		!= '' : Lesson.title 		= json['title']
	if json['description']	!= '' : Lesson.description 	= json['description']
	if json['picture']		!= '' : Lesson.picture 		= json['picture']
	if json['audio']		!= '' : Lesson.audio 		= json['audio']
	if json['background']	!= '' : Lesson.background 	= json['background']
	if json['bibliography'] != '' : Lesson.bibliography = json['bibliography']
	if json['url'] 			!= '' : Lesson.url			= json['url'] 
	db.session.commit()
	return "OK", 200

#Este metodo permite eliminar una leccion
@app.route('/Lesson/Delete/<user_id>/<lesson_id>', methods = ["DELETE"])
def delete_Lesson(user_id,lesson_id):
	print(user_id, type(user_id), lesson_id, type(lesson_id))
	Lesson = Model_Lesson.query.get(int(lesson_id))
	if Lesson.user_id == int(user_id):
		db.session.delete(Lesson)
		db.session.commit()
		return "OK", 200
	else:
		return "It can't be deleted", 204

#Este metodo permite activar y desctivar una leccion
@app.route('/Lesson/Update/is_activate/<lesson_id>', methods = ["PUT"])
def update_Lesson_is_activate(lesson_id):
	Lesson = Model_Lesson.query.get(lesson_id)
	if Lesson is None:
		return "The lesson does not exist", 204
	else:
		Lesson.is_activate = not Lesson.is_activate
		db.session.commit()
		return "The lesson was update", 200