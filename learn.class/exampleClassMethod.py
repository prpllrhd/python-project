#!/usr/bin/env python
'''
example of @classmethod where we are using alternate constructor
refer: https://www.youtube.com/watch?v=rq8cL2XMM5M&index=3&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
'''
class Employee:
	def __init__(self,first,last,salary):
		self.first=first
		self.last=last
		self.salary=salary
	@classmethod
	def fromString(cls,string):
		f,l,s=string.split("-")
		return cls(f,l,s)

emp1 = ("sameer-gawande-50000")
emp2 = ("rakhee-gawande-60440")

newemp1 =  Employee.fromString(emp1)
newemp2 =  Employee.fromString(emp2)
print newemp1.salary
	
		
