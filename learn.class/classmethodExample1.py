from datetime import date

'''
here we are using @classmethod to create instance using a different method. so here the age is not being passed but birthyear.
this is an example of alternate constructor. here you use "fromBirthYear(cls, name, birthYear):" to create an alternate constructor which is "def __init__(self,name,age)" and then all class methods can be used on this.
example issue:
person_str = "sameer:1974". what will you do?
basically you will convert the values so to be able to get name,age
i found this little confusing so the notes

'''

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromstring(cls,namestr):
        name,birthyear = namestr.split(":")
        return cls(name,date.today().year - int(birthyear))

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))



print Person.__dict__

person = Person('Adam', 19)
print person.__dict__
person.display()

person1 = Person.fromBirthYear('John',1985)
print person1.__dict__
person1.display()

newperson = "sameer:1974"
person3 =  Person.fromstring(newperson)
print person3.__dict__
person3.display()
