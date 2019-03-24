'''
using a regular method as well as a class method
simple class method where we are doing alternate constructor where we are getting imput as a string. the goal is to split the string and get fname,lname and salary as instance variables and create a instance from those.
'''
class Employee:
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
	
	@classmethod
	def from_empstring(cls,empstring):
		fname,lname,salary=empstring.split(":")
		return cls(fname,lname,salary)

	def displayemp(self):
		return("employee name is {} {} and salary is {}".format(self.fname,self.lname,self.salary))

emp_string="sameer:gawande:12000"
emp1=Employee("rakhee","gawande",15000)
emp2=Employee.from_empstring(emp_string)
print emp1.displayemp()
print emp2.displayemp()

