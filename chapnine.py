'''
f = open("file.txt")
data = f.read()
print(data)
f.close()
'''

'''
St = ". Ok Rakshit Sawarn but you can try it from Telusko also"
f = open("myfile.txt","w")
f.write(St)
f.close()
'''

'''
f = open("file.txt")
print(f.readlines(),type(f.readlines()))
f.close()
'''

'''
f = open("file.txt")
line = f.readline()
if(line == " "):
    print("No more Lines Left")
else:
    while(line!=""):
        print(line)
        line = f.readline()
f.close()

'''

'''
f = open("file.txt","a")
St = "Big Fool"
f.write(St)
f.close()
'''

'''
with open("file.txt") as f:
    print(f.read())

    ou don't need to close the file here

'''



