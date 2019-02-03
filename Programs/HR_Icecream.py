# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

import bisect
from itertools import combinations
from pprint import pprint


def whatFlavours(c, m):
    """ This is final working solution passing all test cases of HR"""
    hs = {}  # store compliment here.
    for i in range(len(c)):
        if c[i] in hs:  # check for compliment in hash table.
            print(hs[c[i]], i + 1)
            break
        hs[m - c[i]] = i + 1  # store compliments index


whatFlavours([2, 2, 4, 3], 4)
whatFlavours([2, 7, 8, 5, 8, 3, 8], 16)


def whatFlavors1(cost, money):
    """ This passes initial cases, but timesout """
    for i, j in combinations(cost, 2):
        if i + j == money:
            firstIndex = cost.index(i)
            if i == j:
                secondIndex = cost.index(j, firstIndex + 1)
            else:
                secondIndex = cost.index(j)
            print(firstIndex + 1, secondIndex + 1)


# whatFlavors1([1, 4, 5, 3, 2],4)


def whatFlavors2(c, m):
    """ This is not correct"""
    s = set()
    for i in range(len(c)):
        if m - c[i] in c:
            s.add(i)
            s.add(c.index(m - c[i]))
            print(s)


# whatFlavors2([1, 4, 5, 3, 2], 4)


def whatFlavors3(c, m):
    d = dict(enumerate(c, 1))
    pprint(d)
    for i, v in d.items():
        # print(i,v)
        if m - d[i] in d.values():
            print(i)


# whatFlavors3([1, 4, 5, 3, 2], 4)

def whatFlavors4(c, m):
    l1 = [(v, i) for i, v in enumerate(c, 1)]
    l2 = sorted(l1, key=lambda x: x[0])
    print(l2)
    for e in l2:
        comp = m - e[0]
        print(bisect.bisect([e[0] for e in l2], comp, 0, len(l2)))

# whatFlavors4([1, 4, 5, 3, 2], 4)
