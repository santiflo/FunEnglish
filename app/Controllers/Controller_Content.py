from flask import request, jsonify
from pprint import pprint
from app.app import app, db, ma
from app.Models.Model_Content import Model_Content, Schema_Content
from app.Models.Model_Content_Type import Model_Content_Type
from app.Models.Model_Lesson import Model_Lesson, Schema_Lesson

#Este metodo permite crear un Content
@app.route('/Content/Create', methods = ['POST'])
def create_Content():
	json = request.get_json(force=True)
	Content = Schema_Content().load(request.get_json())
	db.session.add(Content)
	db.session.commit()
	return "Content creado", 201

#Este metodo permite listar todos los Contentes
@app.route('/Content', methods = ['GET'])
def all_Content():
	Contents = Model_Content.query.all()
	json = Schema_Content(many=True).dump(Contents)
	return jsonify(json), 200

#Este metodo permite actualizar un Content
@app.route('/Content/Update', methods=['PUT'])
def update_Content():
	json = request.get_json(force=True)
	Content = Model_Content.query.get(json['id'])
	if json['name_Content'] != '': Content.name_Content = json['name_Content']
	if json['describe'] != '': Content.describe = json['describe']
	db.session.commit()
	return "Content updated", 200

#Este metodo permite eliminar un Content
@app.route('/Content/Delete/<Content_id>', methods = ['DELETE'])
def delete_Content(Content_id):
	Content = Model_Content.query.get(Content_id)
	db.session.delete(Content)
	db.session.commit()
	return "OK", 200

#Este metodo permite buscar el contenido segun un tipo de contenido y tipo de leccion
@app.route('/Content/Search/Content_Type/<content_type_id>/Lesson_Type/<lesson_type_id>', methods = ['GET'])
def search_Content_by_Content_Type_n_Lesson_Type(content_type_id, lesson_type_id):
	Lesson = Model_Lesson.query.filter(
		Model_Lesson.lesson_type_id == lesson_type_id
	).with_entities(
		Model_Lesson.id
	)
	lessons = Schema_Lesson(many = True).dump(Lesson)
	lesson_id = [x['id'] for x in lessons]
	Content = Model_Content.query.filter(
		Model_Content.content_type_id == int(content_type_id),
		Model_Content.lesson_id.in_(lesson_id)
	)
	json = Schema_Content(many = True).dump(Content)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

# Este metodo permite buscar el contenido de una leccion por el tipo de contenido
@app.route('/Content/<lesson_id>/<type_name>', methods = ["GET"])
def search_Content_by_Content_Type(lesson_id, type_name):
	Content_Type = Model_Content_Type.query.filter(Model_Content_Type.name.ilike('%'+type_name+'%')).first()
	conten_type_id = Content_Type.id
	print(type_name, conten_type_id)
	Content = Model_Content.query.filter(
		Model_Content.lesson_id == int(lesson_id), 
		Model_Content.content_type_id == conten_type_id
		)
	json = Schema_Content(many = True).dump(Content)
	response = jsonify(json)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response, 200

# Metodo que permite eliminar un contenido
@app.route('/Content/Delete/<content_id>', methods = ["DELETE"])
def Delete_Content(content_id):
	Content = Model_Content.query.get(content_id)
	db.session.delete(Multimedia)
	db.session.commit()
	return "OK", 200

# Metodo que permite subir una imagen 
@app.route('/Content/Upload/Image/<lesson_id>/<user_id>/<text>', methods=['POST'])
def upload_file(virtual_exposition_id, user_id, text):
	# check if the post request has the file part
	if 'file' not in request.files:
		print('archivo vacio')
		flash('No file part')
		return "No existe ninguna imagen en la peticion", 204
	file = request.files['file']
	# If the user does not select a file, the browser submits an
	# empty file without a filename.
	if file.filename == '':
		flash('No selected file')
		print('Archivo sin nombre')
		return "El archivo no cuenta con ningun nombre", 204
	if file and allowed_file(file.filename):
		filename = secure_filename(f'{file.filename}_{lesson_id}_{user_id}')
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		data = {
			'path' : str('https://fun-english-cali.herokuapp.com'+url_for('download_file', name=filename)),
			'text' : text,
			'lesson_id' : int(lesson_id),
			'user_id' : int(user_id),
			'type_id' : 3
		}
		Content = Schema_Content().load(data)
		db.session.add(Multimedia)
		db.session.commit()
		print('Existoso')
		return "Proceso exitoso", 201
	print('error general')
	return "Error a la hora de subir la imgen", 204

# Metodo que verifica la extension del archivo para que reciba solo imagenes
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Metodo que retonar una imagen cuando es solicitada
@app.route('/Images/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)