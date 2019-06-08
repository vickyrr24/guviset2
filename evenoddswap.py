string=input()
new=""
for i in range(0,len(string)-1,2):
    new+=string[i+1]
    new+=string[i]
if(len(string)%2==0):
    print(new)
else:
    print(new+string[len(string)-1])
