# Pattern 1
'''rows = int(input("Enter the number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")'''

# Pattern 2
'''rows = int(input("Enter the number of rows "))
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")'''
    
'''# Pattern 3
rows = int(input("Enter the number of rows "))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
# Pattern 4
rows = int(input("Enter the number of rows "))
i = rows
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

# Pattern 5
rows=int(input("Enter number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        if j<=i:
            print(j, end=' ')
        else:
            break
    print('')
    
# Pattern 6
a=1
for i in range(1,6):
    for j in range(1,6):
        if a>9:
            a=1
        if j<=i:
            print(a, end = '')
        else:
            break
        a=a+1
    print('')
    
# Pattern 7
ascii_number = 65
rows = int(input("Enter the number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")'''

# Pattern 8
n = 0
rows = int(input("Enter number of rows: "))
for m in range(1, rows+1):
   for gap in range(1, (rows-m)+1):
      print(end=" ")
   while n != (2*m-1):
      print("*", end="")
      n = n + 1
   n = 0
   print()
    
# Pattern 9
n=int(input("Enter number of rows: "))
for i in range(1,n+1):
    print(("*"*i).rjust(n),("*"*i).rjust(n))

# Pattern 10
rows=int(input("Enter number of rows: "))
clm=int(input("Enter number of columns: "))
ch=input("Enter any character: ")
for i in range(rows):
    for j in range(clm):
        if(i==0 or i==rows-1 or j==0 or j==clm-1):
            print('%c'%ch,end='')
        else:
            print('',end=' ')
    print()
  
# Pattern 11
rows = int(input("Enter the number of rows "))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
    
# Pattern 12 
rows = int(input("Enter number of rows: "))
sp=0
for i  in range(rows,0,-1):
    print("*"*i+" "*sp*2+"*"*i, end=' ')
    sp+=1
    print()
    
# Pattern of pyramid by different method
rows=int(input("Enter number of rows: "))
sp=8
for i in range(1,rows+1):
    print(" "*sp+"* "*i,end=' ')
    sp-=1
    print()