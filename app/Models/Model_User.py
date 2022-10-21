from app.app import db, ma
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, Boolean
from marshmallow import post_load
from sqlalchemy.orm import relationship
from app.Models.Model_Course import Model_Course
from app.Models.Model_Lesson import Model_Lesson
from app.Models.Model_Content import Model_Content

class Model_User(db.Model):
	#Atributos
	__tablename__ = 'TBL_USER'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	last_name_1 = Column(String(50), nullable = True)
	last_name_2 = Column(String(50), nullable = True)
	type_document = Column(String(2), nullable = False)
	document = Column(String(15), nullable = False, unique = True)
	password = Column(String(128), nullable = False)
	describe = Column(Text, nullable = True)
	picture = Column(Text, nullable = True, default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Stick_Figure.svg/170px-Stick_Figure.svg.png?20070219055013')
	is_active = Column(Boolean, nullable = False, default = True)
	#Foraneos
	rol_id = Column(Integer, ForeignKey('TBL_ROL.id'), nullable = False)
	#Relaciones
	Course = db.relationship('Model_Course', backref ='User', lazy ='dynamic')
	Lesson = db.relationship('Model_Lesson', backref = 'User', lazy = 'dynamic')
	Content = db.relationship('Model_Content', backref = 'User', lazy = 'dynamic')
	#Trigger
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

class Schema_User(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_User
        include_fk = True

    @post_load
    def make_User(self, data, **kwargs):
        return Model_User(**data)