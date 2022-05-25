num=int(input("Enter a number: "))
sqr=num**2
print(f"Square of {num} is {sqr}.")
sum=0
while(sqr>0):
        ldigit=sqr%10
        sum=sum+ldigit
        sqr=sqr//10
print(f"The sum of {sqr} and {ldigit} is {sum}.")
if(sum==num):
        print(f"{num} is a neon number.")