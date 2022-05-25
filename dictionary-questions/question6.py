a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input('enter the key'))
    y=int(input("enter the value"))
    a.update({x:y})
key=int(input("enter the key you want to delete"))
if key in a:
    a.pop(key)
    print(a)
else:
    print("key is not valid")