# Kangroo problem:
# There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# Given the starting locations and movement rates for each kangaroo, can you determine
# if they’ll ever land at the same location at the same time?


x1, v1, x2, v2 = map(int,input().strip().split())

if x1 == x2 and v1 == v2:
    print("YES")
elif x1 == x2 and v1 > v2:
    print("NO")
elif x1 < x2 and v1 < v2:
    print('NO')
elif(x2-x1) % (v2 - v1) == 0:
    print("YES")
else:
    print('NO')




