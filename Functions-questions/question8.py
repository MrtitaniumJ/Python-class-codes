def unique(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return x
a=(input("enter the numbers")).split()
a=list(map(int,a))
c=unique(a)
print(c)