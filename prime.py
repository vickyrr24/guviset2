m,n=[int(x) for x in input().split()]
prime=[True for x in range(n+1)]
for i in range(2,n+1):
    if(prime[i]==True):
        temp=i*2
        count=2
        while(temp<n):
            prime[temp]=False
            temp=i*count
            count+=1
count=0
for i in range(m,n):
    if(prime[i]==True):
        count=count+1
print(count)
