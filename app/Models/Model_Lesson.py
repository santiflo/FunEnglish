from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Content import Model_Content
from app.Models.Model_Comment import Model_Comment

class Model_Lesson(db.Model):
	#Atributos
	__tablename__ = 'TBL_LESSON'
	id = Column(Integer, primary_key = True)
	title = Column(String(100), nullable = False, default = 'blank title')
	description = Column(Text, default = 'blank description')
	creation_date = Column(DateTime, default = datetime.utcnow)
	number_views = Column(Integer, nullable = False, default = 0)
	picture = Column(Text, nullable = True, default = 'Inser image')
	audio = Column(Text, nullable = True, default = '') 
	background = Column(Text, nullable = True, default = '')
	bibliography = Column(Text, nullable = True, default = '')
	url = Column(Text, nullable = True, default = '')
	is_active = Column(Boolean, nullable = False, default = True)
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USER.id'), nullable = False)
	course_id = Column(Integer, ForeignKey('TBL_COURSE.id'), nullable = True)
	lesson_type_id = Column(Integer, ForeignKey('TBL_LESSON_TYPE.id'), nullable = False)
	#Relaciones
	Content = db.relationship('Model_Content', backref = 'Lesson', lazy = 'dynamic', cascade="all, delete-orphan")
	Comment = db.relationship('Model_Comment', backref = 'Lesson', lazy = 'dynamic', cascade="all, delete-orphan")
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Lesson(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Lesson
        include_fk = True

    @post_load
    def make_Lesson(self, data, **kwargs):
        return Model_Lesson(**data)