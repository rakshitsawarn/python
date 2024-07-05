'''
square = lambda x:x*x
print(square(5))
'''

'''
sum = lambda a,b,c:a+b+c
print(sum(1,2,3))
'''

'''
a = ["Harry","Rohan","Subham"]
final = "::".join(a)
print(final)
'''

'''
a = "{} is a good {}".format("Rakshit","Boy")
print(a)
'''

'''
lis = [1,2,3,4,5]
square = lambda x:x*x
squaredlist = map(square,lis)
print(list(squaredlist))
'''

'''
def even(n):
    if(n%2==0):
        return True
    else:
        return False
l = [1,2,3,4,5,6,6,6]
onlyEven = filter(even,l)
print(list(onlyEven))
'''

'''
from functools import reduce
l =[1,2,3,4,5,6,7,8,9]
def sum(a,b):
    return a+b
print(reduce(sum,l))
'''
