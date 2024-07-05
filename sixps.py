'''
#Question - 1 - Find the greatest number input by user
number = int(input("Enter Number 1: "))
number1 = int(input("Enter Number 2: "))
number2 = int(input("Enter Number 3: "))
number3 = int(input("Enter Number 4: "))
if(number>number1 and  number2>number3 and number1>number2):
    print("Number 1 is greatest")
elif(number<number1 and number2<number3 and number<number3):
    print('Number 4 is greatest')
elif(number<number1 and number2>number3 and number1>number2):
    print("Number 2 is greatest")
elif(number<number1 and number2>number3 and number1<number3):
    print("Number 3 is greatest")
else:
    print("All numbers are Equal")
print("Thanks for using us")
'''

'''
#Question - 2 - Write a program to find out whether a student is passed or failed

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter Marks of subject 2: "))
sub3 = int(input("Enter Marks of Subject 3: "))
totalmarks = 300;
if(sub1>=99):
    print("Passed in Sub 1")
else:
    print("Failed in Subject 1")
if(sub2>=99):
    print("Passed in sub 2")
else:
    print("Failed in Subject 2")
if(sub3>=99):
    print("Passed in Subject 3")
else:
    print("Failed in Subject 3")
if(sub1>=99 and sub2>=99 and sub3>=99):
    print("Passed Overall")
else:
    print("Failed Overall")
'''

'''
#Question 3 - Detect Spam Messages

p1 = "Make lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
message = input("Enter Your Message: ")
if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This Comment is a spam")
else:
    print("Thanks for Commenting we appreciate it")

print("Thanks for using us")
'''

'''
#Question 4 - Check whether given username contains 10 characters or not

username = input("Enter your UserName")
if(len(username)>=10):
    print("UserName contains 10 characters")
else:
    print("UserName don't contains 10 Character")
print("Thanks")
'''

'''
#Question 5 - Write a program to find out whether a given name is present in list or not
list = ["Harry","Rohan","Shyam","Mohan"]
if("Harry" in list):
    print("True")
else:
    print("False")
if("Rohan" in list):
    print("True")
else:
    print("False")
if("Shyam" in list):
    print("True")
else:
    print("False")
if("Mohan" in list):
    print("True")
else:
    print("False")
if("Rakshit" in list):
    print("True")
else:
    print("False")
print("Thanks for believing us")
'''

'''
#Question - 6- Grade of student from marks from following scheme
marks = int(input("Enter Marks of Student"))
if(marks<=50):
    print("Your Grade is: F")
elif(50<=marks<=60):
    print("Your Grade is: D")
elif(60<=marks<=70):
    print("Your Grade is: C")
elif(70<=marks<=80):
    print("Your Grade is: B")
elif(80<=marks<=90):
    print("Your grade is: A")
else:
    print("Your Grade is: EX")
'''
#Question - 7 - Whether given post is talking about Harry or not


