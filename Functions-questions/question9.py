def fact(n):
    f=1
    while(n>0):
        f=f*n
        n-=1
    return f
n=int(input("entre the number"))
c=fact(n)
print(c)