from collections import defaultdict

memo = defaultdict(int)

def fibo_dp(n):
    if n == 0 or n == 1:
        return n

    if memo[n] == 0 and n>0:
        memo[n] = fibo_dp(n-1)+fibo_dp(n-2)
    print('Unstacking',n,' memo ',memo[n])
    return memo[n]

print(fibo_dp(5))
