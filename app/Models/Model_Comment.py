from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text, DateTime
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Comment(db.Model):
	#Atributos
	__tablename__ = 'TBL_COMMENT'
	id = Column(Integer, primary_key = True)
	comment = Column(Text, nullable = False)
	date = Column(DateTime, nullable = False, default = datetime.utcnow)
	#Foraneos
	lesson_id = Column(Integer, ForeignKey('TBL_LESSON.id'), nullable = False)
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Comment(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Comment
        include_fk = True

    @post_load
    def make_Comment(self, data, **kwargs):
        return Model_Comment(**data)