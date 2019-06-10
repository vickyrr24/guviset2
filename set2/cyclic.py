n,m=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
for i in range(m):
    lst[0],lst[len(lst)-1]=lst[len(lst)-1],lst[0]
print(*lst)
