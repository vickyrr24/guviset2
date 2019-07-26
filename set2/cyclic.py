n,m=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
m=m%n
temp=lst[-m:]+lst[:-m]
for i in temp:
    print(i,end=" ")
    
