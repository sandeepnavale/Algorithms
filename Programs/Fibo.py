# Genereate fibonacci numbers
def fibo(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        print(a)


fibo(1000)

# Generate n number of fibo numbers
knownNum = {0: 0, 1: 1}


def fib_rec(num):
    if num in knownNum:
        return knownNum[num]
    fibnum = fib_rec(num-1) + fib_rec(num-2)
    knownNum[num] = fibnum
    return fibnum


fib_rec(10)
print(knownNum)


def fibo_gen():
    a, b = 0, 1
    while(True):
        a, b = b, a+b
        yield b


next(fibo_gen())



def getFibo(N):
    v = [1,2]
    while v[-1] < N:
        v.append(v[-1]+v[-2])

    return set(v)

getFibo(500)

# Fibo with dynamic programming
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    print(f'cache {cache}')
    return wrapper

def fibo(n):
    if n < 2: return 1
    return fibo(n-1)+fibo(n-2)


@memo
def fibo_dp(n):
    if n<2: return 1
    return fibo_dp(n-1) + fibo_dp(n-2)

print(fibo_dp(10))