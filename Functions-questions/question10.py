def perfect(n):
    i=1
    sum=0
    while(i<=(n//2)):
        if(n%i==0):
            sum+=i
        i+=1
    if(sum==n):
        return 1
    else:
        return 0
n=int(input("enter the no."))
if perfect(n)==1:
    print("No. is perfect")
else:
    print("No. is not perfect")