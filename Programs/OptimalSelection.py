# Example :
# Input :
# 3
# 5
# 1 2 2 4 9
# Explanation :
# Case 1 :
# First he selects 1
# Points : 1 * 0 (no integer selected before this)
# Total Points = 0
#
# Then he selects 2
# Points : 2 * 1 (1 selected before this)
# Total Points = 2
#
# Then he selects 2
# Points : 2 * 2 (1,2 selected before this)
# Total Points = 6
# 
# Then he selects 4
# Points : 4 * 3 (1,2,2 selected before this)
# Total Points = 18
#
# Then he selects 9
# Points : 9 * 4 (1,2,2,4 selected before this)
# Total Points = 54

# SOLUTION:

t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    res = 0
    for i, v in enumerate(arr):
        res += v * i
    print(res)
