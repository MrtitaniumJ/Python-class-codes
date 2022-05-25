f=open("data.txt", "r")
str = " "
while str:
     str = f.readline()
     print(str, end = "")
f.close()

#Q-- Write a program in Python to copy the entire content from file “data.txt” to “story.txt”
f = open("data.txt", "r")
f1 = open("story.txt", "w")
d = f.read()
f1.write(d)
f.close()
f1.close()