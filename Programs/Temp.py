from itertools import combinations
import sys

n = 7
k = 3
p = [10,100,300,200,1000,20,30,]

def getMin(p,k):
    min_d = sys.maxsize
    for x in combinations(p,k):
        cur_d = 0
        for i in combinations(x,2):
            cur_d += abs(i[0]-i[1])
        if cur_d < min_d:
            min_d = cur_d
            selected = x
            print(selected,cur_d)




def isPalindrome(s):
    sl = len(s)
    a = [[0]*sl for i in range(sl)]
    for i in range(sl):
        a[i][i] = 1

    return a

print(isPalindrome('AAAAA'))
