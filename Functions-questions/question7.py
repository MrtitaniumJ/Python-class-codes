def panagram(str):
    c=0
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return 0
        else:
            c+=1
    if(c==26):
        return 1
str=input("enter the string")
if panagram(str)==1:
    print("string is panagram")
else:
    print("string is not panagram")