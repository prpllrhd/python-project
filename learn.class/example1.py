#!/usr/bin/env python
class Employee:

	payraise = 1.05
	num_of_emp = 0
	def __init__(self,first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary
		Employee.num_of_emp += 1
	
	def fullname(self):
		return ('{}, {}'.format(self.first,self.last))

	def salary_hike(self):
		return (self.salary * self.payraise)


a1 = Employee("sameer","gawande",50000)
a2 = Employee("rakhee","gawande",60000)



	
