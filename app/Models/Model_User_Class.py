from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma

class Model_User_Class(db.Model):
	#Atributos
	__tablename__ = 'TBL_USER_CLASS'
	#Foraneos
	user_id = Column(Integer, ForeignKey('TBL_USER.id'), primary_key=True, nullable = False)
	class_id = Column(Integer, ForeignKey('TBL_CLASS.id'), primary_key=True, nullable = False)
	#Relaciones
	#Triggers

	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Schema_User_Class(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_User_Class
        include_fk = True

    @post_load
    def make_User_Class(self, data, **kwargs):
        return Model_User_Class(**data)