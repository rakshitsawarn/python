'''
# Question - 1 Write the multiplication table of a givn number

a = int(input("Enter the number: "))
for b in range(11):
    print(a * b)
    b+=1
'''

'''
#Question - 2 - Wish them whose name starts with S
l = ["Harry","Soham","Sachin","Rahul"]
a = input("Enter your Name: ")
i = 0
while(i<len(l)):
    if(a.startswith("S")):

        print("GOOD MORNING",a)
else:
    print("Not S")
'''

'''
#Question - 3 - Attempt Question using for loop
l = ["Harry","Soham","Sachin","Rahul"]
a = input("Enter Your Name: ")
i = 0
for i in range(5):
    if a.startswith("S"):
        print("Good Morning, Have a nice day")
    else:
       print("Bad Morning Have a Worst Day")
'''

'''
#Question - 4 - Attempt problem 1 using while loop
a = int(input("Enter Your Number: "))
i = 1
while(i<11):
    print(a*i)
    i+=1
'''

'''
#Question - 5 - Find number is prime or not
a = int(input("Enter the Number: "))
if(a%a == 0 and a%1==0):
    print("Number is Prime")
elif(a<0):
    print("Number is in Negative")
else:
    print("Number is Composite")
'''

'''
#Question - 5 - Method -2 

a = 5
for i in range(2,a):
    if(a%i==0):
        print("Number is not prime")
        i+=1
    else:
        print("Number is Prime")
'''

'''
#Question -6 - Sum of n natural number using while loop
n = int(input("Enter the number: ))
i = 1
sum = 0
while(i<=n):
    i+=1
    sum+=1
print(sum)
'''

'''
#Question - 7 - find factorial of a number
n = int(input("Enter the number: "))
product = 1
for i in range(1,n+1):
    product = product * i
print(f"The factorial of {n} is {product}")
'''

'''
#Question - 8 - print stars for n = 3

n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(""*(n-i),end = "")
    print("*" * (2*i-1),end = "")
    print("")
'''

'''
#Question - 9 - print stars in * ** *** format line by line

n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("*" * i,end  = "")
    print("")
'''

'''
#Question - 10 - print stars in *** * * *** format
n = 3
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end = "")
    else:
        print("*",end="")
        print(" "*(n-2),end = "")
        print("*",end ="")
    print("")
'''

'''
#Question -11 - print multiplication table in reverse order

n = 5
for i in range(1,11):
    print(n*(11-i)))
    i+=1
'''
