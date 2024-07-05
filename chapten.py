'''
class Employee:
    language = "Python"
    salary = 1200000

Rakshit = Employee()
print(Rakshit.language,Rakshit.salary)

rohan = Employee()
rohan.name = "Ser"
print(rohan.name,rohan.salary,rohan.language)
'''

'''
class Employee:
    language = "python" #Class Attribute
    salary = 150 #Class Attribute
    name = "Rak" #Class Attribute
Rakshit = Employee()
Rakshit.language = "Java" #Instance Attribute prefered over Class Attribute
Rakshit.name = "Sawarn" #Instance Attribute prefered over Class Attribute
Rakshit.salary = 1500000000000000000000 #Instance Attribute prefered over Class Attribute
print(Rakshit.language,Rakshit.name,Rakshit.salary)
'''

'''
class Employee:
    salary = 200
    name = "Shyam singh "
    language = "C & C++"
    @staticmethod
    def greet():
        print("Good Morning sir, Here is your information")
    def getInfo(self):
        salary = 200
        name = "Shyam singh "
        language = "C & C++"
        print(f"The name of employee is {self.name}\n The Salary of Employee is {self.salary}\n The language in which employee works is {self.language}\n Thanks and Regards")
obj = Employee()
obj.greet()
obj.getInfo()
'''

'''
class Employe:
    name = "Satyam"
    salary = 23
    language = "Ruby"

    def __init__(self,name,salary,language):
        self.name = "Satyam"
        self.salary = 23
        self.language = "Ruby"
        print("I am a constructor")
    @staticmethod
    def greet():
        print("Good Morning Sir,")
    def getInfo(self):
        name = "Satyam"
        salary = 23
        language = "Ruby"
        print(f"The details demanded by you are: \n Name: {self.name}\n Salary: {self.salary}\n Language: {self.language}")

obj = Employe("Satyam",23,"Ruby")
obj.greet()
obj.getInfo()
'''
