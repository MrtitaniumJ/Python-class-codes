f = open("task.txt", "r")
d = f.read()
va=ve=vo=vu=vi=0
for i in d:
     if i=='a' or i=='A':
         va=va+1
     if i=='e' or i=='E':
         ve=ve+1
     if i=='i' or i=='I':
         vi=vi+1
     if i=='o' or i=='O':
         vo=vo+1
     if i=='u' or i=='U':
         vu=vu+1
print("Frequency of vowel \"a\" is", va)
print("Frequency of vowel \"e\" is", ve)
print("Frequency of vowel \"i\" is", vi)
print("Frequency of vowel \"o\" is", vo)
print("Frequency of vowel \"u\" is", vu)