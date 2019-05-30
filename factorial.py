num=int(input())
def fact(num):
    n=1
    while num>0:
            n=n*num
            num=num-1
    return(n)
print(fact(num))
