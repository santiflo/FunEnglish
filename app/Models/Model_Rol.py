from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, String
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_User import Model_User

class Model_Rol(db.Model):
	#Atributos
	__tablename__ = 'TBL_ROL'
	id = Column(Integer, primary_key = True)
	name_rol = Column(String(50), unique = True, nullable = False)
	describe = Column(Text, nullable = False)
	#Foraneos
	#Relaciones
	db.relationship('Model_User', backref ='Rol', lazy ='dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Rol(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Rol
        include_fk = True

    @post_load
    def make_Rol(self, data, **kwargs):
        return Model_Rol(**data)