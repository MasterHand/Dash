#!/usr/bin/python
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

print sqlalchemy.__version__

engine = create_engine('mysql+mysqldb://root:three3@localhost:1337/TESTDB', echo=False)
Base = declarative_base()

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

#Session object is the 'handle' to the database.
Session = sessionmaker(bind=engine)
session = Session()

#new_emp = Employee(name='AndrewBBBB', age='24', role='Manager', salary='44000', cRate='.30')
#new_emp2 = Employee(name='Michael', age='21', role='Detailer', salary='0', cRate='30')


#new_emp.newEmployee()
#new_emp2.newEmployee()

getEmployee('Michael')

kill=Employee()

kill = session.query(Employee).filter(Employee.name=='Andrew').all()
#print kill

getAllEmployees()

delEmployee('Andrew')



