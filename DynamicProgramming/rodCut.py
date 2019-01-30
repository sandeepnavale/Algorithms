# this example is from CLRS.
# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces

import unittest
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
        for j in range(0, i):
            curProfit = max(curProfit, p[j] + memo[i - j - 1])
        memo[i] = curProfit
    return memo[n]


def cutRod_BU_WithPieces(p, n):
    """ Returns the maximum profit along with rod pieces."""
    memo = defaultdict(int)
    pieces = [0 for _ in range(n + 1)]
    for i in range(1, n + 1): #n+1 as 0 is ignored
        curProfit = 0
        for j in range(1, i + 1): #i+1 as 0 is ignored
            if curProfit < p[j] + memo[i-j]:
                curProfit = p[j] + memo[i-j]
                pieces[i] = j
        memo[i] = curProfit

    # print indexes
    temp = n
    indexs = []
    while temp > 0:
        # print(pieces[temp])
        indexs.append((pieces[temp]))
        temp = temp - pieces[temp]
    # print(memo[n])
    return memo[n], indexs


class RodcutTestCase(unittest.TestCase):
    def testCaseBf(self):
        # Sample price list.
        priceList = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        expectedProfit = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        obtainedProfit = [cutRodBf(priceList, i) for i in range(1, 11)]
        self.assertEqual(expectedProfit, obtainedProfit)

    def testTopDownDp(self):
        priceList = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        expectedProfit = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        obtainedProfit = [cutRodTopDownDP(priceList, i) for i in range(1, 11)]
        self.assertEqual(expectedProfit, obtainedProfit)

    def testTopDownDp(self):
        priceList = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        expectedProfit = [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]
        obtainedProfit = [cutRodBottomUpDP(priceList, i) for i in range(1, 11)]
        self.assertEqual(expectedProfit, obtainedProfit)

    def testcutRod_BU_WithPieces(self):
        priceList2 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual((18, [1, 6]), cutRod_BU_WithPieces(priceList2, 7))
        self.assertEqual((30, [10]), cutRod_BU_WithPieces(priceList2, 10))
        self.assertEqual((10, [2, 2]), cutRod_BU_WithPieces(priceList2, 4))


if __name__ == '__main__':
    unittest.main()

    # Sample price list.
    # priceList = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # for i in range(1, 11):
    # print("BF Maximum profit on length: \t", i, " is ", cutRodBf(priceList, i))
    # print("TD Maximum profit on length: \t", i, " is ", cutRodTopDownDP(priceList, i))
    # print("BU Maximum profit on length: \t", i, " is ", cutRodBottomUpDP(priceList, i))
    # print("BU Maximum profit on length: \t", i, " is ", cutRod_BU_WithPieces(priceList, i))
    # print('\n')
    # priceList2 = [0,1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # print(cutRod_BU_WithPieces(priceList2, 7))
