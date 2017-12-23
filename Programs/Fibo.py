# Genereate fibonacci numbers
def fibo(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        print(a)


fibo(1000)

# Generate n number of fibo numbers
knownNum = {0:0,1:1}
def fib_rec(num):
    if num in knownNum:
        return knownNum[num]
    fibnum = fib_rec(num-1) + fib_rec(num-2)
    knownNum[num]= fibnum
    return fibnum

fib_rec(10)
print(knownNum)