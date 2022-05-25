f=open("data.txt")
d=f.readlines()
for i in d:
   if len(i)>40:
       print(i)