from sqlalchemy import create_engine

#the returned value of create_engine() is an instance of Engine 
#which represents the core interface  to the database
engine = create_engine('sqlite:///memory:', echo=True)

'''Declare a mapping
when using the Object Relational Mapper, the config process starts by describing
the database tables, and then by defining our classes which will be mapped
to those tables
'''
from sqlalchemy.ext.declarative import declarative_base
#maintains a catalog of classes and tables relative to 'Base'
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	password = Column(String)

'''optional: returns a String representation of the object for printing
	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" %(
			self.name, self.fullname, self.password)
'''
Base.metadata.create_all(engine) #create new tables, skip over tables already created

#ed_user = User(name='ed', fullname='ed sherran', password='password')

#print ed_user.name
#print ed_user.fullname
#print ed_user.id

'''
the ORM "handle" to the database is the Session obj.
The session class will serve asa factroy for our new session objects
This custom-made Session class will create new Session objects which are bound
to out database.
'''
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session=Session() #Session is associated with the sqLite engine

'''Adding new objects'''
ed_user = User(name='ed', fullname='ed sherran', password='password')
session.add(ed_user)
'''at this point the instance is pending; no sql has been executed'''

our_user = session.query(User).filter_by(name='ed').first()
print ed_user is our_user#returns true


session.add_all(
	[User(name="andy", fullname="andy berg", password="passwd4"),
	 User(name="abc", fullname="abc xyz", password="lmnop"),
	 User(name="brad", fullname="brad ferrara", password="winall")
	])

print session.new #the session knows 3 objects are pending
session.commit() #flushes whatever remaining changes remain in the db, and commits the transaction

print ed_user.id

for instance in session.query(User).order_by(User.id):
	print instance.id, instance.fullname
	#session.delete(instance)
	#session.commit()   #this clears all data is User Table and commits

'''
Rolling Back
a session works within a transaction, we can roll back changes made.
'''
#if you execute a session and, this will kick the current transaction
#session.rollback()

'''Query
a query object is created using query() method on Session. This function takes
a variable number of args, which can be any combination of classes.

Below we indicate a query which loads 'User' instances.
'''
#for instance in session.query(User).order_by('User.id'):
#	print instance.name, instance.fullname

'''
FILTER OPERATIONS
'''










