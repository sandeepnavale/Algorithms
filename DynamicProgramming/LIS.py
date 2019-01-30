
from itertools import combinations
import timeit

# Longest increasing subsequence -- Brute force
def lis_bruteforce(seq):
    for length in range(len(seq),0,-1):
        for sub in combinations(seq,length):
            # print(sub)
            if list(sub) == sorted(sub):
                return sub

print(lis_bruteforce([3,1,0,2,4]))

# Recursive solution with memoization. - DP.
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def lis_rec(seq):
    @memo
    def lis(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res,1+lis(pre))
        return res

    return max([lis(i) for i in range(len(seq))])

print(f'length of LIS is {lis_rec([3,1,0,2,4])}' )
print(f'length of LIS is {lis_rec([1,0,7,2,8,3,4,9])}' )