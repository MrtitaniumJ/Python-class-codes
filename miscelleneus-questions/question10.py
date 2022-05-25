 lst1=list(map(int, input().split()))
lst=[]
for i in lst1:
    if i not in lst:
        lst.append(i)
    
lst2=list(map(int, input().split()))
lst4=[]
for i in lst2:
    if i not in lst4:
        lst4.append(i)
lst3= list(filter(lambda n: n in lst, lst4))
print(lst3)