'''
#Question -1 - Write a function from which you can check greatest of three numbers

def greatestnumber():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    c = int(input("Enter Number 3: "))
    if(a>b and b>c):
        print("a is greatest")
    elif(a<b and b>c):
        print("b is greatest")
    elif(a>b and b<c and a<c):
        print('C is greatest')
    else:
        print("Enter Valid Number")

greatestnumber()
'''

'''
#Question - 2- Conversion from Celsius to Farenheit

def convert():
    celcius = int(input("Enter Temperature in degree Celcius: "))
    print((celcius*9/5) + 32)

convert()
'''

'''
#Question - 3 - Prevent python function print() to print() new line
def preventnewline():
    a = input("Enter a Sentence: ")
    print(a,end=" ")
preventnewline()
'''

'''
#Question - 4- Recursive function to write the sum of first n natural number

def sumofnaturalnumber():
    n = int(input("Enter a Natural Number: "))
    a = n*(n+1)
    print(a/2)

sumofnaturalnumber()
'''

'''
#Question - 5- print first n line of pattern  *** ** * for n =3

def pattern(n):
    if(n<=0):
        return "Invalid Input"
    print("*" * n)
    pattern(n-1)
       
pattern(5)
'''

'''
#Question - 6 - Convert from inches to centimeter

def inchestocm(inches):
    cm = inches*2.54
    print(cm)
inchestocm(4)
'''

'''
#Qustion - 7 - Remove a name from list

def removelistelement():
    list = ["Harry","Rakshit","Sawarn","Ramu"]
    print(list.remove("Harry"))
    print(list)

removelistelement()
'''

'''
#Question - 8 - Strip from list
def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Harry","Rohan","Subhman","an"]
print(rem(l,"an"))
'''

'''
#Question - 9- Write a Python function to print a multiplication table of a given  number

def table():
    n = int(input("Enter a Number: "))
    for i in range(1,11):
       print(f"{n} X {i} = {n*i}")
table()


'''
