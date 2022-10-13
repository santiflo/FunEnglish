from flask import Flask, make_response, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app import config

#Inicializadores
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app, resources={r"/*": {"origins": "*"}})

#Models
from app.Models import Model_User
from app.Models import Model_Rol
from app.Models import Model_Grade
from app.Models import Model_User_Grade
from app.Models import Model_User_Class
from app.Models import Model_Class
#from app.Models import Model_Virtual_Expositions
#from app.Models import Model_Types
#from app.Models import Model_Multimedia
#from app.Models import Model_Comments
#from app.Models import Model_Questions

#Controllers
from app.Controllers import Controller_User
from app.Controllers import Controller_Rol
#from app.Controllers import Controller_Users
#from app.Controllers import Controller_Login
#from app.Controllers import Controller_Virtual_Expositions
#from app.Controllers import Controller_Types
#from app.Controllers import Controller_Multimedia
#from app.Controllers import Controller_Comments
#from app.Controllers import Controller_Questions