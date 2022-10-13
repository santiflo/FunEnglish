from app.app import app, db
#from app.Models.Model_User import Schema_User
#from app.Models.Model_Types import Schema_Types
from app.Models.Model_Rol import Schema_Rol

def insert_rol():
	student_rol = {
	'name_rol' : 'Student',
	'describe' : 'Student role which allows you to see classes'
	}
	rol = Schema_Rol().load(student_rol)
	db.session.add(rol)
	db.session.commit()

	proffesor_rol = {
	'name_rol' : 'Teacher',
	'describe' : 'Teacher role which allows you to manage students and their classes'
	}
	rol = Schema_Rol().load(proffesor_rol)
	db.session.add(rol)
	db.session.commit()

	admin_rol = {
	'name_rol' : 'Administrator',
	'describe' : 'administrator role which allows you to manage all aplicatio modules'
	}
	rol = Schema_Rol().load(admin_rol)
	db.session.add(rol)
	db.session.commit()

def insert_admin():
	#Usuario administrador
	admin_data = {
	'name': 'administrador', 
	'last_name_1': '', 
	'last_name_2': '', 
	'email': 'admin@admin', 
	'password_hash': '1234', 
	'admin': 1, 
	'born_date': None, 
	'describe': 'Administrador de la aplicacion', 
	'verify_email': True, 
	'picture': 'https://cdn-icons-png.flaticon.com/512/2942/2942813.png'}
	User = Schema_Users().load(admin_data)
	db.session.add(User)
	db.session.commit()
	print('Admin create')

def insert_types():

	# Tipos de datos
	# Subtitle
	subtitle_type = {
	'name' : 'Subtitle',
	'description' : 'Campo de texto que permite crear un subtitulo'
	}
	Type = Schema_Types().load(subtitle_type)
	db.session.add(Type)
	db.session.commit()
	# Video
	video_type = {
	'name' : 'Video',
	'description' : 'Campo de texto que permite cargar la ruta de un video'
	}
	Type = Schema_Types().load(video_type)
	db.session.add(Type)
	db.session.commit()
	# Images
	image_type = {
	'name' : 'Images',
	'description' : 'Campo de texto que permite cargar la ruta de una imagen'
	}
	Type = Schema_Types().load(image_type)
	db.session.add(Type)
	db.session.commit()
	print('Types created')

#db.create_all()
#insert_rol()
#insert_users()
#insert_types()

app.run(debug=True , host="0.0.0.0")