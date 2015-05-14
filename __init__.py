#!/usr/bin/python
import sqlalchemy
#import dbEmployee
#import dbVehicle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#print sqlalchemy.__version__
engine = create_engine('mysql+mysqldb://root:three3@localhost:1337/TESTDB', echo=True)

#Session object is the 'handle' to the database.
Session = sessionmaker(bind=engine)

