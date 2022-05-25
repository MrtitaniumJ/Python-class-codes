a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input('enter the key'))
    y=int(input("enter the value"))
    a.update({x:y})
sum=0
for i in (a.values()):
    sum=sum+i
print('sum','=',sum)