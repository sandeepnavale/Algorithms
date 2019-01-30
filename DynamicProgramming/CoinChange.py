# https://www.youtube.com/watch?v=jaNZ83Q3QGc
"""
Problem
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
S = { S1, S2, .. , Sm} valued //coins, how many ways can we make the change?
The order of coins doesn’t matter.
For example, for N = 4 and S = [1, 2, 3], there are four solutions:
[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3].
So output should be 4.

For N = 10 and S = [2, 5, 3, 6], there are five solutions:
[2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5] and [5, 5].
So the output should be 5.
"""

def CoinChangeDP(amount,coins):
    combinations = [0 for _ in range(amount+1)]
    combinations[0]=1
    for coin in coins:
        for amt in range(amount+1):
            if amt >= coin:
                combinations[amt] += combinations[amt-coin]

    print(combinations[amount])

CoinChangeDP(12,[1,2,5])
CoinChangeDP(5,[1,2,5])

def CoinChangeRec(amount,coins,currentCoin):
    if amount == 0 : return 1
    if amount < 0: return 0
    combi = 0

    for coin in coins:
        combi += CoinChangeRec(amount-coin,coins,coin)

    # for i in range(coin,len)
    return combi

print(CoinChangeRec(4,[1,2],0))

