lst=[]
a=int(input())
for i in range(0,a):
    lst.append(eval(input()))
odd=0
even=0
for i in range(0,a):
    if i%2==0:
        even=even+lst[i]
    else:
        odd=odd+lst[i]
print(f"sum of odd = {odd} \n sum of even = {even}")