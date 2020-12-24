from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np
import math


# calculate slope of line passing through (x1,y1) and (x2,y2).
def slope(x1, y1, x2, y2):
    m = None
    b = y1-y2
    a = x1-x2
    if a != 0:
        m = b/a
    return m

# finding out 3rd vertex of inner smaller triangle where (x1,y1) and (x2,y2) are 1st and 2nd vertex.


def third_point(x1, y1, x2, y2):
    global a
    eq1 = Eq(pow(x-x1, 2)+pow(y-y1, 2)-pow(a/(n+1), 2), 0)
    eq2 = Eq(pow(x-x2, 2)+pow(y-y2, 2)-pow(a/(n+1), 2), 0)
    r = solve((eq1, eq2), (x, y))
    return r

# to decide which point to be considered for next iteration(2 pts will be obtained on solving equation in third_point function).


def check(x1, y1, x, y):
    global x2, y2, x3, y3
    r = (y1-y)*(x3-x2)-(y3-y2)*(x1-x)
    if r < 0:
        return "-ve"
    else:
        return "+ve"


x, y = symbols('x y')
x1, y1, x2, y2, x3, y3 = map(float, input(
    "Enter vertices of equilateral triangle - ").split())
n = int(input("Enter N value - "))
c = check(x1, y1, x2, y2)
a = math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2))
l = [[x2, y2]]
result = []
p = 1
q = n
# finding N vertices that are equally seperated.
for i in range(n):
    l1 = [((p*x3)+(q*x2))/(p+q), ((p*y3)+(q*y2))/(p+q)]
    l.append(l1)
    p = p+1
    q = q-1
l.append([x3, y3])
l1 = []
# 1st iteration to include only 1 point among 2 points that are obtained on solving equations.
for i in range(len(l)-1):
    d = third_point(l[i][0], l[i][1], l[i+1][0], l[i+1][1])
    s = check(d[0][0], d[0][1], x2, y2)
    if c == "+ve" and s == "+ve":
        l1.append([d[0][0], d[0][1]])
        result.append(
            [[l[i][0], l[i][1]], [l[i+1][0], l[i+1][1]], [d[0][0], d[0][1]]])  # final result - coordinates of smaller triangles.
    elif c == "-ve" and s == "-ve":
        l1.append([d[0][0], d[0][1]])
        result.append(
            [[l[i][0], l[i][1]], [l[i+1][0], l[i+1][1]], [d[0][0], d[0][1]]])
    else:
        l1.append([d[1][0], d[1][1]])
        result.append(
            [[l[i][0], l[i][1]], [l[i+1][0], l[i+1][1]], [d[1][0], d[1][1]]])
# general iteration - both points will be considered.
for i in range(n):
    l = []
    for i in range(len(l1)-1):
        d = third_point(l1[i][0], l1[i][1], l1[i+1][0], l1[i+1][1])
        s = check(d[0][0], d[0][1], l1[i][0], l1[i][1])
        if c == "+ve" and s == "+ve":
            l.append([d[0][0], d[0][1]])
        elif c == "-ve" and s == "-ve":
            l.append([d[0][0], d[0][1]])
        else:
            l.append([d[1][0], d[1][1]])
        result.append(
            [[l1[i][0], l1[i][1]], [l1[i+1][0], l1[i+1][1]], [d[0][0], d[0][1]]])
        result.append(
            [[l1[i][0], l1[i][1]], [l1[i+1][0], l1[i+1][1]], [d[1][0], d[1][1]]])
    l1 = []
    l1.extend(l)       # update l1.
lx = []
ly = []
for i in range(len(result)):
    print("Triangle #{}".format(i+1), end=": ")
    for j in result[i]:
        print(j, end=" ")
        lx.append(j[0])
        ly.append(j[1])
    print()
lx.extend([x1, x2, x3])
ly.extend([y1, y2, y3])
tri = [[i, i+1, i+2] for i in range(0, len(lx), 3)]
x = np.asarray(lx, dtype=float)
y = np.asarray(ly, dtype=float)
triang = mtri.Triangulation(x, y, tri)
z = np.cos(1.5 * x) * np.cos(1.5 * y)
plt.tricontourf(triang, z)
plt.triplot(triang, 'ko-')
plt.show()
