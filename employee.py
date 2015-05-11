#!/usr/bin/python
class Employee:

	empCount=0
	def _init_(self, emp_id, first_name, last_name, total_gross, cRate, commission, total_commission):
		self.emp_id = emp_id
		self.first_name = first_name
		self.last_name = last_name
		self.cRate = cRate


		Employee.empCount += 1

	def displayEmp(self):
		print self.emp_id, self.first_name, self.last_name

	def calcCommission(self, cRate, total_gross):

		payment = cRate * total_gross

		return payment

