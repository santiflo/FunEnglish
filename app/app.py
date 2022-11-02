from flask import Flask, make_response, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

#Inicializadores
app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ""
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'Images')
app.config['MAX_CONTENT_LENGTH'] = 4 * 1000 * 1000
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app, resources={r"/*": {"origins": "*"}})

#Models
from app.Models import Model_User
from app.Models import Model_Rol
from app.Models import Model_Grade
from app.Models import Model_Course
from app.Models import Model_Lesson
from app.Models import Model_Lesson_Type
from app.Models import Model_Content
from app.Models import Model_Content_Type
from app.Models import Model_Comment

#Controllers
from app.Controllers import Controller_User
from app.Controllers import Controller_Rol
from app.Controllers import Controller_Login
from app.Controllers import Controller_Course
from app.Controllers import Controller_Grade
from app.Controllers import Controller_Lesson_Type
from app.Controllers import Controller_Lesson
from app.Controllers import Controller_Content_Type
from app.Controllers import Controller_Content


@app.route('/', methods = ['POST','GET'])
def index():
	return '<H1>Hola Jeison</H1>'
