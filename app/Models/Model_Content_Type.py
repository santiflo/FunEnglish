from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Content import Model_Content

class Model_Content_Type(db.Model):
	#Atributos
	__tablename__ = 'TBL_CONTENT_TYPE'
	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False, unique = True)
	description = Column(Text, nullable = False)
	#Foraneos
	#Relaciones
	multimedia = relationship('Model_Content', backref = 'Type', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Content_Type(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Content_Type

    @post_load
    def make_Content_Type(self, data, **kwargs):
        return Model_Content_Type(**data)