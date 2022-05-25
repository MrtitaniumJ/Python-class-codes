f=open("image.txt")
d=f.read()
d=d.split()
c=0
for i in d:
    if i[-1]=='m':
        c=c+1
print("Total words are :", c)
