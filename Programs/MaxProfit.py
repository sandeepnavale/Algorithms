c# Maximum Profit
# Given stock prices list, find maximum profit possible. You can buy and sell multiple times, but you can't hold more than one share at a time. Hint: the solution is really simple, but it's not easy to figure it out - go over some custom test cases by hand and try to see a pattern.
#

def max_profit(prices):
    """Find maximum profit possible."""
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit

assert max_profit([]) == 0
assert max_profit([100]) == 0
assert max_profit([1,6,5,2,8,1,4,5]) == 15
assert max_profit(range(100, 0, -1)) == 0
print('All passed')

