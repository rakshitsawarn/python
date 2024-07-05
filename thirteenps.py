'''
#Question - 1 - Write a program and asks user for phone number, name and marks and format it
a = "The Name of Student is {}. His phone number is {} and his marks is {}".format("Rakshit",7479687456,80)
print(a)
'''

'''
#Question - 2 - A list contains the multiplication table of 7. Write a program to convert it to vertical string of same numbers
table = [str(7*i) for i in range(1,11)]
s = "\n".join(table)
print(s)
'''

'''
#Question - 3 - filter a list of number which is divisible by 5
def divisiable5(n):
    if(n%5==0):
        return True
    return False
a = [1,2,3,4,5,6,7,8,9,10]
f = list(filter(divisiable5,a))
print(f)
'''

'''
#Question - 4 - Use reduce to find the greatest number
from functools import reduce
a = [1,2,3,4,5]
def greater(a,b):
    if(a>b):
        return a
    else:
        return b

print(reduce(greater,a))
'''

'''
#Question - 5 - Explore flask

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p> Hello,World!</p>"
app.run()

'''
