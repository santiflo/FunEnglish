from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, String, Boolean
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Grade(db.Model):
	#Atributos
	__tablename__ = 'TBL_GRADE'
	id = Column(Integer, primary_key = True)
	name_grade = Column(String(50), unique = True, nullable = False)
	describe = Column(Text, nullable = False)
	picture_grade = Column(Text, nullable = True, default = 'Inser image')
	is_active = Column(Boolean, nullable = False, default = True)
	#Foraneos
	#Relaciones
	db.relationship('Model_Course', backref ='Grade', lazy ='dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Grade(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Grade
        include_fk = True

    @post_load
    def make_Grade(self, data, **kwargs):
        return Model_Grade(**data)