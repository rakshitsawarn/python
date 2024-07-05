'''
#Question - 1 - open 3 files and pass a message without exiting

with (
    open("file.txt", "w") as f,
    open("myfile.txt", "w") as f1,
    open("ren.txt", "w") as f2
):
    f.write("This is file.txt\n")
    f1.write("This is myfile.txt\n")
    f2.write("This is ren.txt\n")
'''

'''
#Question -2 - Write a program to print 3rd,5th and 7th element from a list using enumerate

list = [1,2,3,4,5,6,7,8]

for index,items in enumerate(list):
    if(index==2 or index == 4 or index == 7):
        print(f"The Index is:  {index} and the items is {items}")
    else:
        print(" ")
'''

'''
#Question - 3 - Write a list comprehension to print a list which contains the multiplication table of a user entered number
n = int(input("Enter the Number: "))
for i in range(1,11):
    print(f"The Table of {n} is :")
    print(f"{n*i}")
'''

'''
#Question - 4- Write a program to display a/b where if b = 0 display infinte by handling zerodivision error

a = 5
b =5
if(b==0):
    raise ZeroDivisionError("Can't divided by zero")
else:
    print(f"The division result is {a/b}")
'''

#Question - 5 - Store the multiplication table generateed in question 3 in a file named table.txt
n = int(input("Enter  a number: "))
with open("table.txt","a") as f:
    for i in range(1,11):
        a = n*i
        print(a)
        f.write(str(a) + "\n")

