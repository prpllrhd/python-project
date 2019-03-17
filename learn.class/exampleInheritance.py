#!/usr/bin/env python3
class Employee:

	raise_amount = 1.05
	def __init__(self,first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.email = self.first+'_'+self.last+'@company.com'
	
	def print_fullname(self):
		return('{} {}'.format(self.first,self.last))
	
	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)

class Developer(Employee):
	raise_amount = 1.10
	def __init__(self,first,last,salary,prog_lang):
		super().__init__(first,last,salary)
		self.prog_lang = prog_lang
	

emp1 = Employee("abhijeet","jadhav",25000)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)
dev1 = Developer("sameer","gawande",500000, "python")
print(dev1.salary)
dev1.apply_raise()
print(dev1.salary)
	
