x,n=map(int,input("Enter x,n values : ").split())
prod=x
res=0
for i in range(n):
    res=res+(1/prod)
    prod=prod*x
print(res)
