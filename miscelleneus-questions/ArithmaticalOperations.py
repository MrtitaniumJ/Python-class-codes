# 1. WAP to print Hello World!
'''print("Hello World!")'''

# 2. WAP to do arithmetical operations.
'''Arithmetic operations like:
-> Addition
-> Subtraction
-> Multiplication
-> Division
# Store input numbers:
num1=input("Enter first number: ")
num2=input("Enter second number: ")

# Add two numbers ->
sum=float(num1)+float(num2)
sum=float(num1)+float(num2)
# Subtract two numbers ->
min=float(num1)-float(num2)
# Multiply two numbers ->
mul=float(num1)*float(num2)
# Divide two numbers ->
div=float(num1)/float(num2)
#Display the sum, substraction, multiplication, division.
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
print('The division of {0} and {1} is {2}'.format(num1, num2, div))
'''

# 3. WAP to find the area of the triangle.
# Area of triangle = (s*(s-a)*(s-b)*(s-c))-1/2
# Three sides of the triangle is a, b and c:
a=float(input('Enter first side: '))
b=float(input('Enter second side: '))
c=float(input('Enter third side: '))

# Calculate the semi-perimeter
s=(a+b+c)/2

# Calculate the area
area = (s*(s-a)*(s-b)*(s-c))*0.5
print('The area of the triangle is %0.2f'%area)


# Sercond method to find the area of the triangle:
# Input the height and base of the triangle.
h=float(input("Enter the height: "))
b=float(input("Enter the base: "))
a=(h*b)*0.5
print('The area of the triangle is %0.2f'%a)
