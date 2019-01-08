import sys
from itertools import combinations

n = 7
k = 3
p = [10, 100, 300, 200, 1000, 20, 30, ]


def getMin(p, k):
    min_d = sys.maxsize
    for x in combinations(p, k):
        cur_d = 0
        for i in combinations(x, 2):
            cur_d += abs(i[0] - i[1])
        if cur_d < min_d:
            min_d = cur_d
            selected = x
            print(selected, cur_d)


def isPalindrome(s):
    sl = len(s)
    a = [[0] * sl for i in range(sl)]
    for i in range(sl):
        a[i][i] = 1

    return a


print(isPalindrome('AAAAA'))


def two_Strings(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return 1 if set1 & set2 else 0


print(two_Strings('hello', 'world'))
print(two_Strings('hi', 'world'))


def isPalindrome(a):
    length = len(a)
    for i in range(length // 2):
        if a[i] != a[~i]:
            return False
    return True;


# isPalindrome('baab')


