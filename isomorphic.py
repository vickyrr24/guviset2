from collections import Counter
n,m=input().split()
if(Counter(n)==Counter(m)):
    print("yes")
else:
    print("no")
