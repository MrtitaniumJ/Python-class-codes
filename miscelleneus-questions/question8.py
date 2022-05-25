lst1=[]
lst2=[]
n1=int(input())
n2=int(input())
for i in range(0,n1):
    lst1.append(eval(input()))
for i in range(0,n2):
    lst2.append(eval(input()))
lst1[0],lst2[0]=lst2[0],lst1[0]
print(lst1, "\n", lst2)