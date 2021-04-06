def next_num(series):
    size=len(series) + 1
    if size%2==0:
        num=(size+1)*(size+1)-1
    else:
        num=(size-1)*(size-1)+1
    return num
series=list(map(int,input("Enter numbers in the series : ").split()))
print("Next number in the series is {}".format(next_num(series)))
