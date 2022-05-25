a={}
n=int(input("entre the size"))
for i in range(n):
    key=int(input())
    value=int(input())
    a.update({key:value})
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)