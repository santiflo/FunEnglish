from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_User(db.Model):
	#Atributos
	__tablename__ = 'TBL_USER'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	last_name_1 = Column(String(50), nullable = True)
	last_name_2 = Column(String(50), nullable = True)
	type_document = Column(String(2), nullable = True)
	document = Column(String(15), nullable = False, unique = True)
	password = Column(String(128), nullable = False)
	describe = Column(Text, nullable = True)
	picture = Column(Text, nullable = True, default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Stick_Figure.svg/170px-Stick_Figure.svg.png?20070219055013')
	#Foraneos
	rol_id = Column(Integer, ForeignKey('TBL_ROL.id'), nullable = False)
	#Trigger
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

class Schema_User(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_User

    @post_load
    def make_User(self, data, **kwargs):
        return Model_User(**data)