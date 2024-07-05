'''
#Question -1 - Write a program to create a dictionary of hindi words with values as their english translation
dict = {"kela":"Banana","aam":"Mango","santara":"Orange"}
d = input("Enter the word: ")
print(dict[d])
'''

'''

#Question 2 - Write user input of numbers and show them only once
s = {}
s1 = int(input("Enter Number1: "))
s.add(int(s1))
s2 = int(input("Enter Number1: "))
s.add(int(s2))
s3 = int(input("Enter Number1: "))
s.add(int(3))
s4 = int(input("Enter Number1: "))
s.add(int(s4))
s5 = int(input("Enter Number1: "))
s.add(int(s5))
s6 = int(input("Enter Number1: "))
s.add(int(s6))
print(type(s),s)

'''

'''
#Question - 3 - Is it possible that in a set int 18 and Str 18 took place
set = {18,"18"}
print(set)
'''

'''
#Question - 4 - What is the length of set 
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s.__len__()) #Mine
print(len(s)) #Harry
'''

'''
#Question - 5 - type 
s = {}
print(type(s))
'''

'''
#Question - 6  - create an empty dictionary and allow 4 friends to enter their favorite language as values and use key as their name

dict = {}
name = input("Enter Your Name: ")
lang = input("Enter Your fav language: ")
dict.update({name:lang})
name1 = input("Enter Your Name: ")
lang1 = input("Enter Your fav language: ")
dict.update({name1:lang1})
name2 = input("Enter Your Name: ")
lang2 = input("Enter Your fav language: ")
dict.update({name2:lang2})
name3 = input("Enter Your Name: ")
lang3 = input("Enter Your fav language: ")
dict.update({name3:lang3})
print(dict)
print(type(dict))
'''

'''
#Question 7 - What will happen if key will samme
#Value will update 

dict = {}
name = input("Enter Your Name: ")
lang = input("Enter Your Language: ")
dict.update({name:lang})

name1 = input("Enter Your Name: ")
lang1 = input("Enter Your Language: ")
dict.update({name1:lang1})

name2 = input("Enter Your Name: ")
lang2 = input("Enter Your Language: ")
dict.update({name2:lang2})

name3 = input("Enter Your Name: ")
lang3 = input("Enter Your Language: ")
dict.update({name3:lang3})

name4 = input("Enter Your Name: ")
lang4 = input("Enter Your Language: ")
dict.update({name4:lang4})

name5 = input("Enter Your Name: ")
lang5 = input("Enter Your Language: ")
dict.update({name5:lang5})

print(dict)
'''

'''
#Question - 8 - What will happen if values will same
# Nothing will happen
dict = {}
name = input("Enter Your Name: ")
lang = input("Enter Your Language: ")
dict.update({name:lang})

name1 = input("Enter Your Name: ")
lang1 = input("Enter Your Language: ")
dict.update({name1:lang1})

name2 = input("Enter Your Name: ")
lang2 = input("Enter Your Language: ")
dict.update({name2:lang2})

name3 = input("Enter Your Name: ")
lang3 = input("Enter Your Language: ")
dict.update({name3:lang3})

name4 = input("Enter Your Name: ")
lang4 = input("Enter Your Language: ")
dict.update({name4:lang4})

name5 = input("Enter Your Name: ")
lang5 = input("Enter Your Language: ")
dict.update({name5:lang5})
print(dict)
'''

'''
#Question - 9 - Change a value inside a list which is contained in set s
s = {8,7,12,"Harry",[1,2]}
print(s)
Error
'''

