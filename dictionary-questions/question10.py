dict1={}
size=int(input("enter size"))
for i in range(0,size):
    key=int(input())
    value=int(input())
    dict1.update({key:value})
print(max(dict1.values()),' ',end="")
print(min(dict1.values()),' ',end="")