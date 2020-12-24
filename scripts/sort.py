def sort(l1):
    for i in range(len(l1)):
        for j in range(len(l1)-i-1):
            if l1[j][1] > l1[j+1][1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
    return l1


n = int(input('Enter size of list : '))
l = []
for i in range(n):
    l.append(tuple(map(int, input().split())))
print(sort(l))
