'''
#Question - 1 Create a class 2 D vector and use it in creating other class 3D vector

class vector:
    side = 2 
    shape = "square"
    def show(self):
        print(f"The side of 2D vector is {self.side} and its shape is {self.shape}")

class vectorD(vector):
    size = 4
    area = "Bihar"
    def showi(self):
        print(f"{self.size}\n{self.area}")

a = vectorD()
a.showi()
a.show()
'''

'''
#Question - 2 - Create a class pets from a class animals and further create a class Dog and add a method bark to it
class Animals:
    leg = 4
    ears = 2
    horns = 5
    def Info(self):
        print(f"Every Animals have these things and this number: {"Legs are: ",self.leg}\n{"Horns are: ",self.horns}\n{"Ears are: ", self.ears}")
class pet(Animals):
    type = "domestic"
    color = "white"
    number = 5
    def petsInfo(self):
        super().__init__()
        print(f"Every pet is of type {self.type}\n color: {self.color}\n number: {self.number}")

class dog(pet):
    speak = "Bark"
    teeth = "sharp"
    def dogsInfo(self):
        super().__init__()
        print(f"Every pet dog is of type {self.type}\n speaks: {self.speak}\ncolor: {self.color}\n number: {self.number} and have teeth: {self.teeth}")

obj = dog()
obj.dogsInfo()
'''

'''
#Question - 3- Create a class Employee  and add a salary and increment properties to it 
class Employee:
    salary = 234
    increment = 20
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary* (self.increment/100))
    @salaryafterincrement.setter
    def increment(self,salary):
        self.increment = ((salary/self.salary)-1)*100




e = Employee()
e.salaryafterincrement = 280
print(e.salaryafterincrement)
'''

#Question - 4 - write a class complex for complex number which should overloaded by + and * for operations
class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i


    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"
        
    
c1 = complex(1,2)
c2 = complex(3,4)
print(c1+c2)