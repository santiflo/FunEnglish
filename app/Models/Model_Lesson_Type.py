from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Lesson import Model_Lesson

class Model_Lesson_Type(db.Model):
	#Atributos
	__tablename__ = 'TBL_LESSON_TYPE'
	id = Column(Integer, primary_key = True)
	name = Column(String(100), nullable = False, unique = True)
	description = Column(Text, nullable = False)
	#Foraneos
	#Relaciones
	Lesson = relationship('Model_Lesson', backref = 'Lesson_Type', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Lesson_Type(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Lesson_Type

    @post_load
    def make_Lesson_Type(self, data, **kwargs):
        return Model_Lesson_Type(**data)