# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces

from collections import defaultdict


def cutRodBf(price, n):
    """ This is Brute force recursive approach, which has exponential runtime. """
    if n <= 0:
        return 0
    max_val = 0
    for i in range(n):
        max_val = max(max_val, price[i] + cutRodBf(price, n - i - 1))
    return max_val


def cutRodTopDownDP(p, n):
    """TopDown DP uses memoization & recursions"""
    memo = defaultdict(int)
    if memo[n] != 0:
        return memo[n]
    max_val = 0
    for i in range(n):
        max_val = max(max_val, p[i] + cutRodTopDownDP(p, n - i - 1))
    memo[n] = max_val
    return max_val


def cutRodBottomUpDP(p, n):
    """ This is an bottom Up approach of DP which solves smaller subproblems first."""
    memo = defaultdict(int)
    for i in range(1, n + 1):
        curProfit = 0
        for j in range(1, i):
            curProfit = max(curProfit, p[j] + memo[i - j - 1])
        memo[i] = curProfit
    return memo[n]


# Tests.
# Sample price list.
priceList = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

for i in range(1, 11):
    print("BF Maximum profit on length: \t", i, " is ", cutRodBf(priceList, i))
    print("TD Maximum profit on length: \t", i, " is ", cutRodTopDownDP(priceList, i))
    print("BU Maximum profit on length: \t", i, " is ", cutRodBottomUpDP(priceList, i))
    print('\n')

