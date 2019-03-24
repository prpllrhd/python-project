#!/usr/bin/env python
class Date:
	def __init__(self,day=0,month=0,year=0):
		self.day=day
		self.month=month
		self.year=year
	
	@classmethod
	def from_string(cls,date_as_string):
		day,month,year = date_as_string.split("-")
		return cls(day,month,year)

	def displaydate(self):
		return ('{}-{}-{}'.format(self.day,self.month,self.year))

	
dtstr = "15-02-2016"
date2 = Date.from_string(dtstr)
print date2.displaydate()
