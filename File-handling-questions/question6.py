f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] == 'M' or i[0] == 'T':
        c=c+1
print("Total lines are :", c)

#Q--Write a program in python to count those lines from the file “div.txt” which are not starting from ‘M’.
f=open("div.txt")
d=f.readlines()
c=0
for i in d:
     if i[0] != 'M':
         c=c+1
print("Total lines are :", c)
