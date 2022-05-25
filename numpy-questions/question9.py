import numpy as np
row=int(input("Enter number of row: "))
column=int(input("Enter number of column: "))
a=[]
for i in range(row):
    l=list(map(int,input("Enter matrix 1: ").split()))
    a.append(l)
b=np.array(a)
row1=int(input("Enter number of rows: "))
column1=int(input("Enter number of column: "))
a1=[]
for j in range(row1):
    l1=list(map(int, input("Enter matrix 2: ").split()))
    a1.append(l1)
b1=np.array(a1)
c=np.dot(b, b1)
print(c)