from sympy import symbols, Eq, solve


def slope(x1, y1, x2, y2):
    m = None
    b = y1-y2
    a = x1-x2
    if a != 0:
        m = b/a
    return m


x, y = symbols('x y')
x1, y1, x2, y2, x3, y3 = map(float, input().split())
mid_pt1 = list([(x2+x3)/2, (y2+y3)/2])
mid_pt2 = list([(x1+x3)/2, (y1+y3)/2])
m1 = (y1-mid_pt1[1])/(x1-mid_pt1[0])
m1 = slope(x1, y1, mid_pt1[0], mid_pt1[1])
m2 = slope(x2, y2, mid_pt2[0], mid_pt2[1])
if m1:                                    # condition to check if slope is infinite.
    eq2 = Eq(y-y1-m1*x+m1*x1, 0)          # equation of perpendicular bisector.
else:
    eq2 = Eq(x-x1, 0)
if m2:                                    # condition to check if slope is infinite.
    eq1 = Eq(y-y2-m2*x+m2*x2, 0)          # equation of perpendicular bisector.
else:
    eq1 = Eq(x-x2, 0)
# intersection point of perpendicular bisectors(circumcenter).
center = solve((eq1, eq2), (x, y))
print(center)
