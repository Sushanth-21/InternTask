def power(x,i):
    if i==1:
        return x
    else:
        return x*power(x,i-1)
def sigma(x,n):
    res=0
    for i in range(1,n+1):
        res=res+(1/power(x,i))
    return res
x,n=map(int,input("Enter x,n values : ").split())
print(sigma(x,n))
