#!/bin/python3

import math
import os
import random
import re
import sys
#
# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any  numbers in S' is not
#  evenly divisible by k.
#
# Input Format

# The first line contains  space-separated integers,  and , the number of values in  and the non factor.
# The second line contains  space-separated integers describing , the unique values of the set.


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    r = [0] * k

    for value in S:
        r[value % k] += 1

    result = 0
    for a in range(1, (k + 1) // 2):
        result += max(r[a], r[k - a])
    if k % 2 == 0 and r[k // 2]:
        result += 1
    if r[0]:
        result += 1
    return result

def otherMethod(k,arr):
    # n, k = map(int, raw_input().strip().split(" "))
    # arr = map(int, raw_input().strip().split(" "))

    residuals = [i % k for i in arr]
    counter = [0] * k
    for r in residuals:
        counter[r] += 1

    # max one element with residual 0
    c = min(counter[0], 1)

    for i in range(1, (k // 2) + 1):
        if i != k - i:
            c += max(counter[i], counter[k - i])
        else:
            c += min(counter[i], 1)

    print(c)

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    S = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, S)
    print(result)
    res2 = otherMethod(k,S)
    print(res2)