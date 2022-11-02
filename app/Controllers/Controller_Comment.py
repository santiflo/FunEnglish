from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Comment import Model_Comment, Schema_Comment

#Este metodo permite crear un tipo de leccion
@app.route('/Comment/Create', methods = ["POST"])
def create_Comment():
	json = request.get_json(force=True)
	Comment = Schema_Comment().load(json)
	db.session.add(Comment)
	db.session.commit()
	return "Creado", 201

#Este metodo permite listar todas los tipos de lecciones
@app.route('/Comment', methods = ["GET"])
def all_Comment():
	Comment = Model_Comment.query.all()
	json = Schema_Comment(many = True).dump(Comment)
	return jsonify(json), 200

#Este metodo permite buscar un tipo de leccion mediante su id
@app.route('/Comment/Search/id/<comment_id>', methods = ["GET"])
def search_Comment_id(comment_id):
	Comment = Model_Comment.query.get(comment_id)
	json = Schema_Comment().dump(Comment)
	return jsonify(json), 200

#Este metodo permite buscar un comentario mediante el lesson_id
@app.route('/Comment/Search/course_id/<lesson_id>', methods = ["GET"])
def search_Comment_id(lesson_id):
	Comment = Model_Comment.query.filter(Model_Comment.lesson_id == lesson_id)
	json = Schema_Comment().dump(Comment)
	return jsonify(json), 200

#Este metodo permite actualizar una leccion
@app.route('/Comment/Update', methods = ["PUT"])
def update_Comment():
	json = request.get_json(force=True)
	Comment = Model_Comment.query.get(json['id'])
	if json['name']			!= '' : Comment.title 			= json['title']
	if json['description'] 	!= '' : Comment.description 	= json['description']
	if db.session.commit()
	return "OK", 200

#Este metodo permite eliminar una leccion
@app.route('/Comment/Delete/<Comment_id>', methods = ["DELETE"])
def delete_Comment(Comment_id):
	Comment = Model_Comment.query.get(Comment_id)
	db.session.delete(Comment)
	db.session.commit()
	return "OK", 200