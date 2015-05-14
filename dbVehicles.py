#!/usr/bin/python
import sqlalchemy
from __init__ import Session, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadaa.create_all(engine)

session = Session()

class Vehicle(Base):

	__tablename__ = 'vehicles'

		vin = Column(Integer, primary_key = True)
		make = Column(String(20))
		model = Column(String(20))
		year = Column(String(4))

		cust_id = Column(Integer, ForeignKey('customers.id'))


class Customer(Base):
	
	__tablename__ = 'customers'

		id = Column(Integer, primary_key= True)
		name = Column(String(25))
		email = Column(String(25))


