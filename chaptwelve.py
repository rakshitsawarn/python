'''
#Walrus
if(n:= len([1,2,3,4,5])) > 3:
    print(f"The {n} is greter than 3")
else:
    print("Flase")
'''

'''
#types
n: int = 5

name : str = "Rakshit Sawarn"

def sum(a: int, b: int) -> int:
    return a+b
'''

'''
from typing import List,Tuple,Dict,Union

numbers: List[int] = [1,2,3,4,5]
person: Tuple[str,int] = ("Alice", 500)
scores : Dict[str,int] = {"Alice":500,"Bob":510}
identifier: Union[str,int] = "IO98"
'''

'''
def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return("Error")
        case 420:
            return("Chor")
        case _:
            return "Unknown Status"

print(https_status(400))
'''

'''
dict1 = {"Rakshit":500, "Sawarn":"2000"}
dict2 = {"Uf":400,"Samsung":"5000"}
merged = dict1|dict2
print(merged)
'''

'''
with(
    open("file.txt") as f,
    open("myfile.txt") as f1
):
'''

'''
try:
    a = int(input("Enter a Number: "))
except Exception as e:
    print(e,"Please give valid Input")
'''

'''
a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))
if(b==0):
    raise ZeroDivisionError("Sorry Cannot be divided by zero")
else:
    div = (f"The result after division is: {a/b}")
    print(div)
'''

'''
try:
    a = int(input("Enter a Number: "))
except Exception as e:
    print(e)
else: #This is executed only when try block is successfull
    print('I AM INSIDE ELSE') 
'''

'''
def main():
    try:
        a = int(input("Enter a Number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("I am inside Finally Block")

main()
'''

'''
a = 89
def fun():
    global a
    a = 3
    print(a)

print(a)
fun()
'''

'''
l = [1,2,3,4,5,6,7]
for index, item in enumerate(l):
    print(f"The number at {index} is {item}")
'''

'''
mylist = [1,2,3,4,5,6]
squaredList=[]
for item in mylist:
    squaredList.append(item*item)
print(squaredList)
'''
