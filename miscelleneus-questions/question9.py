num=int(input())
lst=[]
for i in range(1, 11):
    lst.append(i)
lst1=list(map(lambda n:n*num,lst))
print(lst1)