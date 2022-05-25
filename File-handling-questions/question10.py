f=open("sample.txt",'r')
n=int(input("entre the no. of lines"))
for i in range(n):
    content=f.readline()
    print(content)
f.close()