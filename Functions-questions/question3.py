def count(word):
    c=d=0
    for i in word:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            c+=1
        elif i>='A' or i<='Z' and  i>='a' or i<='z':
            d+=1
    print("no. of vowels are :",c)
    print("no. of consonants are :",d)
word=input("enter the word :")
count(word)