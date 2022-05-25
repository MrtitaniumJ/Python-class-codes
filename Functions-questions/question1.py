def order_reverse(str):
    str.reverse()
    return " ".join(str)
str=input("entre the string").split()
c=order_reverse(str)
print(c)