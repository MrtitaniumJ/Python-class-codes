a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input('enter the key'))
    y=int(input("enter the value"))
    a.update({x:y})
b={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input('enter the key'))
    y=int(input("enter the value"))
    b.update({x:y})
b.update(a)
print(b)