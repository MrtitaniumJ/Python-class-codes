a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=input('enter the key')
    y=input("enter the value")
    a.update({x:y})
for i in sorted(a.keys()):
    print(i,end="")
print()