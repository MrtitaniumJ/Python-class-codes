dict1={}
size=int(input("enter size"))
for i in range(0,size):
    key=int(input())
    value=int(input())
    dict1.update({key:value})
dict2={}
size=int(input("enter size"))
for i in range(0,size):
    key1=int(input())
    value2=int(input())
    dict2.update({key1:value2})
for i,j in dict2.items():
    dict1[i]=j
print(dict1)