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

class Manager(Employee):
	raise_amount = 1.20
	def __init__(self,first,last,salary,employees=None):
		super().__init__(first,last,salary)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_employee(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print("---->", emp.print_fullname())


	

emp1 = Employee("abhijeet","jadhav",25000)
print(emp1.salary)
emp1.apply_raise()
print(emp1.salary)
dev1 = Developer("sameer","gawande",500000, "python")

print(dev1.salary)
dev1.apply_raise()
print(dev1.salary)
	
man1 = Manager("ravi","shastri",75000,[dev1])
man1.add_employee(emp1)
man1.add_employee(dev1)
man1.remove_employee(emp1)
man1.print_emp()
print(man1.salary)
