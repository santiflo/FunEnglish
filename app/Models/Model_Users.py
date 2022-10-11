from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from marshmallow import post_load
from app.app import db, ma
from app.Models.Model_Virtual_Expositions import Model_Virtual_Expositions
from app.Models.Model_Multimedia import Model_Multimedia
from app.Models.Model_Comments import Model_Comments
from app.Models.Model_Questions import Model_Questions

class Model_User(db.Model):
	#Atributos
	__tablename__ = 'TBL_USER'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	last_name_1 = Column(String(50), nullable = True)
	last_name_2 = Column(String(50), nullable = True)
	identification = Column(String(15), nullable = False, unique = True)
	tipo_identificacion = Column(String(2), nullable = False)
	password = Column(String(128), nullable = False)
	describe = Column(Text, nullable = True)
	picture = Column(Text, nullable = True, default = '')
	#Foraneos
	rol_id = Column(Integer, ForeignKey('TBL_ROL.id'), nullable = False)
	#Relaciones
	#Trigger        
	#	__table_args__ = (db.CheckConstraint('length("password") >= 7', name='password_min_length')
	
	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self = self))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)	

class Schema_User(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Model_User

    @post_load
    def make_User(self, data, **kwargs):
        return Model_User(**data)

