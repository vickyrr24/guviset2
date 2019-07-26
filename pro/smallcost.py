n = input()
n=n.split(" ")
st1=n[0]
st2=n[1]
cost=0
if(st1==st2):
    print(0)
else:
    if(st1<st2):
        st1,st2=st2,st1
    print(st1)
    for i in range(len(st1)):
        if(st1[i]!=st2[i]):
            cost +=1
    cost=cost+(abs(len(st1)-len(st2)))
    print(cost)
            
