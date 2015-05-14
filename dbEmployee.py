#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base


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

	def delAllEmployee(self):
		try:
			for emp in session.query(Employee).order_by(Employee.id):
				session.delete(emp)
				session.commit()

		except NoResultsFound, e:
			print e




#pass in a string, gets first row
def delEmployee(empName):
	try:
		emp = session.query(Employee).filter(Employee.name==empName).first()
		session.delete(emp)
		session.commit()

	except NoResultFound, e:
		print e

#pass in a string, gets first row
def getEmployee(empName):
	try:
		emp = session.query(Employee).filter(Employee.name==empName).first()
		print emp.name, emp.age, emp.role, emp.salary, emp.cRate

	except NoResultsFound, e:
		print e


#lists all employees
def getAllEmployees():
		try:
			for emp in session.query(Employee).order_by(Employee.id):
				print emp.name, emp.age, emp.role, emp.salary, emp.cRate

		except NoResultsFound, e:
			print e

Base.metadata.create_all(engine)


#new_emp = Employee(name='Andrew Bergeron', age='24', role='Manager', salary='44000', cRate='0')

#new_emp.newEmployee()
getEmployee('Michael')

kill=Employee()

kill = session.query(Employee).filter(Employee.name=='Andrew').all()
#print kill

getAllEmployees()

delEmployee('Michael')



