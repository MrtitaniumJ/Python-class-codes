num=int(input("Enter a number: "))
num1=num
sum1=0
sum2=0
i=1
while(num1>0):
        sum1=sum1+(num%10)
        num1=num1//10
        sum2=sum2+(num%10)
        num1=num1//10
if(sum1==sum2):
        print(f"{num} is a magic number.")
else:
        print(f"{num} is not a magic number.")