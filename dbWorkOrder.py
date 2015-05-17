#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from dbVehicle import Customer, Vehicle
from sqlalchemy import Column, Integer, Float, String, update, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
session = Session()

class WorkOrder(Base):

	__tablename__ = 'workorders'

	id = Column(Integer, primary_key = True)
	date = Column(DateTime, default = func.now())
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
			session.add(self)
			session.commit
		except NoResultFound, e:
			session.rollback()
			print e




Base.metadata.create_all(engine)

WO = WorkOrder(DateTime, service='Radiance', addon= '25', vehicle='9384570', cust='1', technician='49')

WO.newWorkOrder()





