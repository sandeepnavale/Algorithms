# Genereate fibonacci numbers
def fibo(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        print(a)


fibo(1000)
