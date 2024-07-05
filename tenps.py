'''
#Question - 1- Make a class named Programmers and store information of programmers working for Microsoft
class Programmers:
    def __init__(self, name, salary, uid, language):
        self.name = name
        self.salary = salary
        self.uid = uid
        self.language = language

    @staticmethod
    def greet():
        print("Good Morning sir, Here is your desired information")

    def getInfo(self):
        print(f"Programmer Name: {self.name}\nProgrammer Unique ID: {self.uid}\nProgrammer Salary: {self.salary}\nProgrammer Domain: {self.language}")

programmer1 = Programmers("Virat Kohli", 100000000, 1, "Ruby, R, Python, and Java")
programmer2 = Programmers("Rohit Sharma", 1, 1234, "C and C++")
Programmers.greet()
programmer1.getInfo()
print() 
programmer2.getInfo()
'''

'''
#Question - 2 - Write a class calculator which can find square square root cube cube root of any number
import math
class calculator():
    a = int(input("Enter a number: "))
    square = a*a
    cube = a*a*a
    squareroot = math.sqrt(a)
    cuberoot = a**1/3
    def calculate(self):
        print(f"The Square of the given number is {self.square}.\n The Cube of a given number is {self.cube}.\n The Square Root of a given number is {self.squareroot}.\n The cube root of a given number is {self.cuberoot}.")

obj = calculator()
obj.calculate()
'''

'''
#Question -3 - create a class with a class attribute a create an object and set a = 0. Does this change class attribute
class a():
    skill = 5
    phone = 10
    def infoA(self):
        print(f"Skill level is : {self.skill}\n Have phone: {self.phone}")

obj = a()
obj.skill = 15
obj.phone = 20
obj.infoA()
'''

'''
#Question - 4- Add a static method in problem 2 to greet the user with hello

import math
class calculator():
    a = int(input("Enter a Number: ))
    square = a*a
    square_root = math.sqrt(a)
    cube = a*a*a
    cube_root = a**1/3
    @staticmethod
    def greet():
        print("Welcome Dear User\n Hope you will like it")
    def calculate(self):
        print(f"The Square of {self.a} is {self.square}.\n The Cube of {self.a} is {self.cube}.\n The Square Root of {self.a} {self.square_root}.\n The cube root of {self.a} is {self.cube_root}.")
        print("Thanks for Believing us!")

obj = calculator()
obj.greet()
obj.calculate()
'''

'''
#Question 5 - Book a train ticket,fare and status
import random

class Train:
    def __init__(self, name, trainNo):
        self.name = name
        self.trainNo = trainNo

    def book(self, passenger_name, fro, to):
        print(f"Ticket is Booked for {passenger_name} in {self.name}\nFrom: {fro}\nTo: {to}")

    def status(self):
        print(f"Train {self.name} (Train No: {self.trainNo}) is running on time")

    def fare(self, fro, to):
        fare_amount = random.randint(500, 5000)
        print(f"Ticket fare in {self.name}\nFrom: {fro}\nTo: {to} is {fare_amount}")
fro = input("Enter Departure Station Name: ")
to = input("Enter Destination Station Name: ")
passenger_name = input("Enter Passenger Name: ")

train = Train(name="Rajdhani Express", trainNo=1111111)

train.book(passenger_name, fro, to)
print()

train.status()
print() 
train.fare(fro, to)
'''

'''
#Question - 6 - What will happen if we will change self
import random

class Train:
    def __init__(self, name, trainNo):
        self.name = name
        self.trainNo = trainNo

    def book(self, passenger_name, fro, to):
        print(f"Ticket is Booked for {passenger_name} in {self.name}\nFrom: {fro}\nTo: {to}")

    def status(self):
        print(f"Train {self.name} (Train No: {self.trainNo}) is running on time")

    def fare(rakshit, fro, to):
        fare_amount = random.randint(500, 5000)
        print(f"Ticket fare in {rakshit.name}\nFrom: {fro}\nTo: {to} is {fare_amount}")
fro = input("Enter Departure Station Name: ")
to = input("Enter Destination Station Name: ")
passenger_name = input("Enter Passenger Name: ")

train = Train(name="Rajdhani Express", trainNo=1111111)

train.book(passenger_name, fro, to)
print()

train.status()
print() 
train.fare(fro, to)
'''
