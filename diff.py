m,n=input().split()
c=0
if(len(m)>len(n)):
    le=len(n)
else:
    le=len(m)

for i in range(0,le):
    if m[i]!=n[i]:
        c+=1
c=c+abs(len(m)-len(n))
if c>1:
    print("no")
else:
    print("yes")
