A, B = map(int, input().split())
l = [i for i in range(1, A+1)]
if A == B:
    print(l)
else:
    l = l[:B-1]+[max(l)]+l[B-1:len(l)-1]
    print(l)
