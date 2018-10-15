import timeit
# find the Maximum subarray sum in O(n)

arr = [-1, 2, 4, -3, 5, 2, -5, 2]
best = 0
n = len(arr)

starttime1 = timeit.default_timer()
# Solution :1
# O(n3) solution.

for a in range(0, n):
    for b in range(a, n):
        sum1 = 0
        for k in range(a, b):
            sum1 += arr[k]

            best = max(best, sum1)

print(best)
print("Method 1 took", timeit.default_timer()-starttime1)


starttime2 = timeit.default_timer()
# Best Solution 2:
# O(n) solution.
sum2 = 0
best2 = 0
for k in range(0, n):
    sum2 = max(arr[k], sum2 + arr[k])
    best2 = max(best2, sum2)
q
print(best2)
print("Method 2 took", timeit.default_timer()-starttime2)
