'''
class Employee:
    company = "ITC"
    def show(self):
        print(f"The salary is {self.salary}")

class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = programmer()
print(a.company,b.company)
'''

'''
class Employee:
    company = "ITC"
    salary = 1000
    def show(self):
        print(f"The Salary is:{self.salary}")

class coder:
    language = "Python"
    def printlanguages(self):
        print(f"Language for coders is: {self.language}")

class programmer(Employee,coder):
    company = "ITC INFOTECH"
    def showLanguage(self):
        print(f"The language is {self.language}")

a = Employee()
b = programmer()

b.show()
b.showLanguage()
b.printlanguages()
'''

'''
class Employee:
    a = 1
class programmer(Employee):
    b = 2
class manager(programmer):
    c = 3

o = Employee()
p = programmer()
q = manager()
print(q.a,q.b,q.c)
print(p.a)
print(p.b)
#print(o.b) #Will show there is no b 
'''

'''
class Employee:
    def __init__(self):
        print("I am a constructor of Employee")
    a = 1
class manager(Employee):
    def __init__(self):
        print("I am a constructor of Manager")
        super().__init__()
    b = 1
class programmer(manager):
    def __init__(self):
        print("I am a constructor of Programmer")
        super().__init__()
    c = 1

o = programmer()
print(o.a, o.b)
'''

'''
class method:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

b = method()
b.a = 45
b.show()
'''

'''
class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of {cls.a} is")
    @property
    def name(self):
        return f"{self.name}{self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
e.name = "Rakshit Sawarn"
print(e.fname,e.lname)
e.show
'''


