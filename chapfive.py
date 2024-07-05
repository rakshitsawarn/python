'''
marks = {
    "Harry":100,
    "Rohan":99,
    "Sohan":56,
    "Mohan":88
}
marks.update({"Harry":99,"Renu":60})
print("Marks of Harry is: ",marks["Harry"]) #If we will use Harry2 which is not in dictionary it will show error
print("Items are: ",marks.items())
print(marks.get("Harry")) #If we will use Harry2 which is not in dictionary it will show none
print("Keys are: ",marks.keys())
print(marks)
'''

'''
set = {1,2,3,4}
print(type(set))
#set = () Empty set
'''

'''
set = {1,2,3,4}
set.add(234)
set.remove(234)
print(set)
'''
set1 = {1,2,3,4}
set2 = {1,123,234,456,789}
print(set1-set2)
print(set1.union(set2))
print(set1.intersection(set2))
