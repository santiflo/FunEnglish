from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Text
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_Class(db.Model):
	#Atributos
	__tablename__ = 'TBL_CLASS'
	id = Column(Integer, primary_key = True)
	name_class = Column(String(50), unique = True, nullable = False)
	describe = Column(Text, nullable = False)
	#Foraneos
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_Class(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_Class
        include_fk = True

    @post_load
    def make_Class(self, data, **kwargs):
        return Model_Class(**data)