#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

session = Session()

class Vehicle(Base):

	__tablename__ = 'vehicles'

	vin = Column(Integer, primary_key = True)
	make = Column(String(20))
	model = Column(String(20))
	year = Column(String(4))

	cust_id = Column(Integer, ForeignKey('customers.id'))

	def __repr__(self):
		return "<Vehicle(vin='%s', make='%s', model='%s', year='%s', cust_id='%s')>" % \
					(self.vin, self.make, self.model, self.year, self.cust_id)

	def newCar(self):
		try:
			session.add(self)
			session.commit()

		except NoResultFound, e: #rollback an integrity constraint on foreign key
			session.rollback()
			print e

class Customer(Base):
	
	__tablename__ = 'customers'

	id = Column(Integer, primary_key= True)
	name = Column(String(25))
	email = Column(String(25))

	def __repr__(self):
		return "<Customer(name='%s', email='%s')>" % \
				(self.name, self.email)


	def newCustomer(self):
		try:
			session.add(self)
			session.commit()

		except NoresultFound, e:
			session.rollback()
			print e

Base.metadata.create_all(engine)


'''
new_cust= Customer(name='Big Berggy', email='FUCK@gmail.com')
session.add(new_cust)
session.commit()
'''

new_car = Vehicle(vin='7687418', make='Suzuki', model='GSXR 1000', year='2008', cust_id='2')
new_car.newCar()



