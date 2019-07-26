n=int(input())
lst=[]
ma=""
t=""
for i in range(0,n):
    temp = input()
    lst.append(temp)
for i in range(0,n-1):
    st1=lst[i]
    st2=lst[i+1]
    if(len(st1)>len(st2)):
        st1,st2=st2,st1
    for i in range(len(st1)):
        if(st1[i]==st2[i]):
            t +=st1[i]
        else:
            break
    if(len(ma)<len(t)):
        ma=""
        ma=t
    t=""
print(ma)
            
    
        
    
