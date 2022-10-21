from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import Integer, Text
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Content(db.Model):
	#Atributos
	__tablename__ = 'TBL_CONTENT'
	id = Column(Integer, primary_key = True)
	path = Column(Text, nullable = True)
	text = Column(Text, nullable = True)
	#Foraneos
	lesson_id = Column(Integer, ForeignKey('TBL_LESSON.id'), nullable = False)
	user_id = Column(Integer, ForeignKey('TBL_USER.id'), nullable = False)
	content_type_id = Column(Integer, ForeignKey('TBL_CONTENT_TYPE.id'), nullable = False) # Titulo = 1, Texto = 2, Video = 3, Audio = 4, Imagen = 5 y Subtitulo = 6
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Content(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Content
        include_fk = True

    @post_load
    def make_Content(self, data, **kwargs):
        return Model_Content(**data)