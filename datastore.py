#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from sqlalchemy import Column, Integer, String, Float, update, DateTime, func, ForeignKey
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref



Base = declarative_base()

session = Session()

class Employee(Base):
	__tablename__ = 'employees'

	#Declarative provides a built in __init__() method 
	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)
	age = Column(Integer)
	role = Column(String(20))
	salary = Column(Integer)
	cRate = Column(Integer)

	#returns a String representation of the object for printing
	def __repr__(self):
		return "<Employee(name='%s', age='%s', role='%s', salary='%s', cRate='%s')>" % \
					(self.name, self.age, self.role, self.salary, self.cRate)

	#creates a new employee
	def newEmployee(self):
		try:
			session.add(self)
			session.commit()

		except e:
			session.rollback()
			print e

	def bulkDelEmployee(self):
		try:
			for emp in session.query(Employee).order_by(Employee.id):
				session.delete(emp)
				session.commit()

		except NoResultsFound, e:
			print e

#pass in a string, employee name
def delEmployee(empName):
	try:
		emp = session.query(Employee).filter(Employee.name==empName).first()
		session.delete(emp)
		session.commit()

	except NoResultFound, e:
		print e

#pass in a string, employee name
def getEmployee(empName):
	try:
		emp = session.query(Employee).filter(Employee.name==empName).first()
		print emp.name, emp.age, emp.role, emp.salary, emp.cRate

	except NoResultFound, e:
		print e


#lists all employees
def getAllEmployees():
		try:
			for emp in session.query(Employee).order_by(Employee.id):
				print emp.name, emp.age, emp.role, emp.salary, emp.cRate

		except NoResultFound, e:
			print e

def updateEmployee(emp_id, name, age, role, salary, cRate):
	try:
		session.query(Employee).filter(Employee.id == emp_id).\
			update({"name": name,
					"age": age,
					"role": role,
					"salary": salary,
					"cRate": cRate
					}, synchronize_session='evaluate')
		session.commit()
	except NoResultFound, e:
		print e



















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

		except NoResultFound, e:
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
















class WorkOrder(Base):

	__tablename__ = 'workorders'

	id = Column(Integer, primary_key = True)
	date = Column(String(10))
	service = Column(String(25))
	addon = Column(Integer)

	vehicle = Column(Integer, ForeignKey('vehicles.vin'))
	cust = Column(Integer, ForeignKey('customers.id'))
	technician = Column(Integer, ForeignKey('employees.id'))
	



	def __repr__(self):
		return "<WorkOrder(date='%s', service='%s', addon='%s', vehicle='%s', cust='%s',technician='%s')>" %\
					(self.date, self.service, self.addon, self.vehicle, self.cust, self.technician)


	def newWorkOrder(self):
		try:
			print "calling newWorkOrder"
			session.add(self)
			session.commit()

		except NoResultFound, e:
			session.rollback()
			print e

def delWorkOrder(wo_id):
	try:
		wo = session.query(WorkOrder).filter(WorkOrder.id == wo_id).first()
		session.delete(wo)
		session.commit()
	except NoResultFound, e:
		print e

def getWorkOrder(wo_id):
	try:
		wo = session.query(WorkOrder).filter(WorkOrder.id ==wo_id).first()
		#print wo
		print wo.date, wo.service, wo.addon, wo.vehicle, wo.cust, wo.technician
	except NoResultFound, e:
		print e


def updateWorkOrder(wo_id, date, service, addon, vehicle, cust, technician):
	try:
		session.query(WorkOrder).filter(WorkOrder.id==wo_id).\
			update({"date":date,
				"service": service,
				"addon": addon,
				"vehicle": vehicle,
				"cust": cust, 
				"technician": technician
			}, synchronize_session='evaluate')
		session.commit()
	except NoResultFound, e:
		print e









Base.metadata.create_all(engine)

#newCust= Customer(name="John", email='Boberson')
#newCust.newCustomer()

#newcar = Vehicle(vin='12345', make='Nissan', model='Altima', year='2006', cust_id='5')
#newcar.newCar()

#WO = WorkOrder(date='2015-05-17',service='Radiance', addon= '100', vehicle='12345', cust='5', technician='50')
#WO.newWorkOrder()

#getWorkOrder('1')

#new_emp = Employee(name='Andrew Bergeron', age='24', role='Manager', salary='44000', cRate='0')

#new_emp.newEmployee()
#getEmployee('Michael')

#kill=Employee()

#kill = session.query(Employee).filter(Employee.name=='Andrew').all()
#print kill

#getAllEmployees()

#delEmployee('Michael')



