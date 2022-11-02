from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Content_Type import Model_Content_Type, Schema_Content_Type

#Este metodo permite crear un tipo de contenido
@app.route('/Content_Type/Create', methods = ['POST'])
def create_Content_Type():
	json = request.get_json(force=True)
	Content_Type = Schema_Content_Type().load(request.get_json())
	db.session.add(Content_Type)
	db.session.commit()
	return "Content_Type creado", 201

#Este metodo permite listar todos los tipos de contenidos
@app.route('/Content_Type', methods = ['GET'])
def all_Content_Type():
	Content_Types = Model_Content_Type.query.all()
	json = Schema_Content_Type(many=True).dump(Content_Types)
	return jsonify(json), 200

#Este metodo permite actualizar un tipo de contenido
@app.route('/Content_Type/Update', methods=['PUT'])
def update_Content_Type():
	json = request.get_json(force=True)
	Content_Type = Model_Content_Type.query.get(json['id'])
	if json['text'] != '': Content_Type.name_Content_Type = json['text']
	if json['path'] != '': Content_Type.describe = json['path']
	db.session.commit()
	return "Content_Type updated", 200

#Este metodo permite eliminar un tipo de contenido
@app.route('/Content_Type/Delete/<Content_Type_id>', methods = ['DELETE'])
def delete_Content_Type(Content_Type_id):
	Content_Type = Model_Content_Type.query.get(Content_Type_id)
	db.session.delete(Content_Type)
	db.session.commit()
	return "OK", 200