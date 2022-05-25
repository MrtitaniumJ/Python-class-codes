def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
a=int(input())
b=int(input())
c=int(input())
d=max(a,b,c)
print(d)