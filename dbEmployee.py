#!/usr/bin/python
import MySQLdb

#open the database connection
db = MySQLdb.connect("localhost", "root", "three3", "TESTDB")

cursor = db.cursor()

cursor.execute("drop table if exists employee")

makeTable ="""CREATE TABLE EMPLOYEE (
				name varchar(20) not null,
				age int,
				role varchar(20),
				salary float,
				cRate float,
				total_gross float )"""

cursor.execute(makeTable)

name=raw_input ("name:" )
age=raw_input("age:" )
role=raw_input("role:" )
salary=raw_input("salary:" )
cRate=raw_input("cRate:") 

newEmp= "insert into employee(name, age, role, salary, cRate)\
			VALUES ('%s', '%s', '%s', '%s', '%s')" % \
			(name,age,role,salary,cRate)

try:
	cursor.execute(newEmp)
	db.commit()
except:
	db.rollback()


#showEmp= """select * from employee"""

#cursor.execute(showEmp)

cursor.execute("select version()")

data = cursor.fetchone()

print "Db version : is %s" %data
db.close()