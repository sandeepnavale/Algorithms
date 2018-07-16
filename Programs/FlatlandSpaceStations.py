# https://www.hackerrank.com/challenges/flatland-space-stations/forum

# Flatland is a country with a number of cities, some of which have space stations.
# Cities are numbered consecutively and each has a road of 1km length connecting it to the next city.
# It is not a circular route, so the first city does not connect with the last city.
# Determine the maximum distance from any city to it's nearest space station.
#
# For example, there are n=3 cities and  m =1of them has a space station, city 1. They occur consecutively along a route.
# City2  is  2-1 unit away and city3  is 3-1=2 units away.
# City1  is  0 units from its nearest space station as one is located there. The maximum distance is 2.

import math

def helper(l, r):
    res = 0;
    if r - l == 1:
        return 0
    for i in range(l+1, r):
        res = max(res, min(i-l , r-i))
    return res

def sol1(n,m,c):

    l = r = 0
    res = c[0]
    for i in range(1, m):
        l = c[i-1]
        r = c[i]
        res = max(res , helper(l, r))
    return (max(res, n-c[m-1]-1))

def sol2(n,m,c):
    c.sort()
    global_max = 0
    L = len(c)
    for i in range(0, L + 1):
        if (i == 0):
            local_max = c[i] - 0
        elif (i == L):
            local_max = (n - 1) - c[L - 1]
        elif (c[i] - c[i - 1] > 1):
            local_max = math.floor((c[i] - c[i - 1]) / 2)
        if (local_max > global_max):
            global_max = local_max

    return(global_max)


if __name__ == '__main__':
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = sorted(map(int, input().strip().split(' ')))

    print(sol1(n,m,c))
    print(sol2(n,m,c))