'''
#Question - 1 - Take 7 fruits name from users
fruits = []
f1 = input("Enter name of fruit: ")
fruits.append(f1)
f2 = input("Enter name of fruit: ")
fruits.append(f2)
f3 = input("Enter name of fruit: ")
fruits.append(f3)
f4 = input("Enter name of fruit: ")
fruits.append(f4)
f5 = input("Enter name of fruit: ")
fruits.append(f5)
f6 = input("Enter name of fruit: ")
fruits.append(f6)
f7 = input("Enter name of fruit: ")
fruits.append(f7)
print(fruits)
'''

'''
#Question - 2 - Take marks of 6 students and display them insorted way

marks = []
m1 = int(input("Enter marks of student 1: "))
marks.append(m1)
m2 = int(input("Enter marks of student 1: "))
marks.append(m2)
m3 = int(input("Enter marks of student 1: "))
marks.append(m3)
m4 = int(input("Enter marks of student 1: "))
marks.append(m4)
m5 = int(input("Enter marks of student 1: "))
marks.append(m5)
m6 = int(input("Enter marks of student 1: "))
marks.append(m6)
marks.sort()
print(marks)
'''

'''
#Question-3 - Check that Tuple type can't be changed in python
tuple = (1,2,3,4,5,True,"Sharma","Verma",False)
tuple[2] = 1000
print(tuple) #Tuple is immutable and can't be changed
print(type(tuple))
'''

'''
#Question - 4- Sum of a list

list = [1,2,3,4]
print(sum(list))
'''

'''
#Question - 5 - Write a program to count total number of zeros
a = (7,0,8,0,0,9)
print(a.count(0))
'''
