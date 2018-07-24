def arrayManupulation(n,q):
    a = [0]* (n+1)
    sum1 = 0
    max1 = 0
    for start,end,value in q:
        # print(start,end,value)
        a[start] += value

        if end+1 <= n:
            a[end+1] -= value

    for x in a:
        # print(x)
        sum1 += x
        max1 = max(max1,sum1)
    return max1



n = 10
q = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

print(arrayManupulation(n,q))

n1 = 4
q1 = [[2, 3, 603], [1, 1, 286],[4, 4, 882]]

print(arrayManupulation(n1,q1))
