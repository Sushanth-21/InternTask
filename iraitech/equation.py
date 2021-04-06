def equation(x,y,n):
    if n==1:
        return (x/y)
    else:
        return (x/y)*equation(x,y,n-1)
x,y,a,b=map(int,input("Enter x,y,a,b values : ").split())
# On simplifying the given equation, it is mathematically equal to (x/y) multiplies ab times i.e., power((x/y),a*b)
n=a*b
print("Result of the equation is {}".format(equation(x,y,n)))
