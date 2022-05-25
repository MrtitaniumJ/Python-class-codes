n=int(input("Enter a number: "))
i=1
sum=0
while(i<n/2):
        if(n%i==0):
                sum=sum+i
                i=i+1
if(sum==n):
        print(f"{n} is perfect number.")
else:
        print(f"{n} is not a perfect number.")