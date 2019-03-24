'''
using a regular method in a class
'''
class Employee:
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary

	def printemp(self):
		return ("the name is {} {} and salary is {}".format(self.fname,self.lname,self.salary))

emp1=Employee("sameer","gawande",12000)
print Employee.printemp(emp1)
