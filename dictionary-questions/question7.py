a={}
size=int(input("enter the size :"))
for i in range(0,size):
    x=int(input("entre the key"))
    y=int(input("entre the value"))
    a[x]=y
key=int(input("enter the replacement key"))
a.pop(key)
key1=int(input("enter the key"))
value1=int(input('enter the value'))
a[key1]=value1
print(a)