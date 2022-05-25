import math
n=eval(input("Enter a number: "))
num=n
l=math.log(n, 10)+1
#i=1
sum=0
while(num>0):
        temp=num%10
        sum=sum+(temp**l)
        num=n//10
if(sum==n):
        print(f"{n} is an Armstrong number.")
else:
        print(f"{n} is not an Armstrong Number")