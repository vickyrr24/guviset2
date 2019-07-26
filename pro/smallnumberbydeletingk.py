from itertools import combinations
n = input()
n=n.split(" ")
nu = n[0]
k = int(n[1])
mi=int(nu)
if ( k == 0):
    print(nu)
else:
    c = combinations(list(nu),len(str(nu))-k)
    c = list(c)
    for i in c:
        temp="".join(map(str,i))
        if(mi>int(temp)):
            mi=int(temp)
print(mi)
    
