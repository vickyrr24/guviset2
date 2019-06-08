string=input()
new=""
for i in range(0,len(string)-1,2):
    new+=string[i+1]
    new+=string[i]
print(new)
