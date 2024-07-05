'''
#Question - 1 - Write a program to read it from a file and find whether word twinkle present in it or not

with open("file.txt") as f:
    
    if("twinkle" in f.read()):
        print("Twinkle word in present")
    else:
        print("It is not present")
        print(f.read())
'''

'''
#Question - 2- The game() function in a program lets user play a game and return a score in integer format . You need to read a file which is either blank or contain the previous high score you need to write a program to  update the hi score wheneer game function will break it 
import random
def game():
    print("You are playing the game....")
    score = random.randint(1,62)
    with open("file.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your Score: {score}")
    if(score>hiscore):
        with open("file.txt","w") as f:
            f.write(str(score))
    return score
game()
'''

'''
#Question - 3 - Write table for 2 to 20 and place it in diffrent files
for n in range(2, 21):
    filename = f"table_of_{n}.txt"
    with open(filename, "w") as f:
        for i in range(1, 11):
            table = f"{n} X {i} = {n*i}\n"
            f.write(table)
'''

'''
#Question - 4 - Replace word donkey by ###
with open("myfile.txt") as f:

    data = f.read()
    if("donkey" in data):
            
            data.replace("donkey","###")
    else:
            
            print("Fine")

with open("myfile.txt","w") as f:
    f.write(data.replace("donkey","###"))
'''

'''
#Question - 5 - Replace # for list of sensored words
words = ["donkey","bad","worst","idiot","nonsense","shit"]

with open("sensored.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"@#$%")

with open("sensored.txt","w") as f:
    f.write(content)
'''

'''
#Question - 6 - Check whether in file python contains or not - Method 1

with open("log.txt") as f:
    a = f.read()
    print(a.find("python"))

'''

'''
#Question - 6 - Check whether in file python contains or not - Method 2
with open("log.txt") as f:
    b = f.read()
    if("python" in b):
        print("Yes,There is word python in this file")
    else:
        print("No, Python ")
'''

'''
#Question - 7- Check the line number when python present in Question - 6
with open("log.txt")as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes,{lineno}")
        break
    lineno+=1
else:
    print("No")
'''

'''
#Question - 8 - make a copy of file
with open("log.txt") as f:
    content = f.read()

with open("myfile.txt","w") as f:
    content_copy = f.write(content)
    print(content_copy)
'''

'''
#Question - 9 - See whether contents of 2 file matching or not

with open("log.txt") as f:
    content = f.read()

with open("myfile.txt") as f:
    content_copy = f.read()

    if(content == content_copy):
        print("Yes, Both are same")
    else:
        print("No,You made an error")
'''

'''
#Question - 10 - Wipe out the content of a file

with open("file.txt","w") as f:
    print(f.write(" "))
'''

'''
#Question - 11 - Write a program to rename a file 
with open("ren.txt") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(content)


'''
