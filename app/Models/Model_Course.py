from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, String, Boolean
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Lesson import Model_Lesson

class Model_Course(db.Model):
	#Atributos
	__tablename__ = 'TBL_COURSE'
	id = Column(Integer, primary_key = True)
	name_course = Column(String(50), unique = True, nullable = False)
	describe = Column(Text, nullable = False)
	picture_course = Column(Text, nullable = False, default = 'Inser image')
	is_active = Column(Boolean, nullable = False, default = True)
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USER.id'), nullable = False)
	grade_id = Column(Integer, ForeignKey('TBL_GRADE.id'), nullable = False)
	#Relaciones
	Lesson = db.relationship('Model_Lesson', backref = 'Course', lazy = 'dynamic')
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Course(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Course
        include_fk = True

    @post_load
    def make_Course(self, data, **kwargs):
        return Model_Course(**data)