#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from sqlalchemy import Column, Integer, String, ForeignKey, update
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

	#pass in vin number
	def bulkDelCars(self):
		try:
			for car in session.query(Vehicle).order_by(Vehicle.vin):
				session.delete(car)
				session.commit()

		except NoResultFound, e:
			print e

#pass in vin number
def deleteCar(carName):
	try:
		carvin = session.query(Vehicle).filter(Vehicle.vin ==argName).first()
		session.delete(carvin)
		session.commit()

	except NoResultFound, e:
		print e

#pass in vin number
def getCar(carName):
	try:
		carvin = session.query(Vehicle).filter(Vehicle.vin==carName).first()
		print carvin.vin, carvin.make, carvin.model, carvin.year, carvin.cust_id
	except NoResultFound, e:
		print e


def getAllCars():
	try:
		for car in session.query(Vehicle).order_by(Vehicle.vin):
			print car.vin, car.make, car.model, car.year, car.cust_id
	except NoResultFound, e:
		print e



#UPDATE you might need to only 1 of these, use text box will prefilled data and edit what you need to edit.
#pass in strings
def updateCar(carName, vin, make, model, year, cust_id):
	print vin, make, model, year, cust_id
	try:
		session.query(Vehicle).filter(Vehicle.vin == carName).\
						update({"vin":vin,
								"make": make, 
								"model": model,
								"year": year,
								"cust_id": cust_id	
								},synchronize_session='evaluate')
		 
		session.commit()
	except NoResultFound, e:
		print e









class Customer(Base):
	
	__tablename__ = 'customers'

	id = Column(Integer, primary_key= True)
	name = Column(String(25), nullable=True)
	email = Column(String(25), nullable=True)

	automobiles = relationship("Vehicle", backref = "customers")

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


#pass in customer name string
def deleteCustomer(custName):
	try:
		person = session.query(Customer).filter(Customer.name==custName).first()
		session.delete(person)
		session.commit()
	except NoResultFound, e:
		print e
#pass in customer name string
def getCustomer(custName):
	try:
		person = session.query(Customer).filter(Customer.name==custName).first()
		print person.name, person.email
	except NoResultFound, e:
		print 

#pass in strings
def updateCustomer(cust_id, name, email):
	try:
		session.query(Customer).filter(Customer.id==cust_id).\
			update({"name":name,
					"email": email
				}, synchronize_session='evaluate')
		session.commit()
	except NoResultFound, e:
		print e




Base.metadata.create_all(engine)

print "dbVehicle script is executed"

#updateCar("11111", "11111", "Kawasaki", "Ninja ZX-6R", "2015", "1")

#updateCustomer("3", "Big Daddy", "apb@ghotmail.com")

#new_cust= Customer(name='Big Berggy', email='FUCK@gmail.com')
#session.add(new_cust)
#session.commit()


#new_car = Vehicle(vin='222222', make='Suzuki', model='GSXR 1000', year='2008', cust_id='1')
#new_car.newCar()


