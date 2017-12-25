def array_left_rotation(a, n, k):
    for i in range(k):
        poped = a[0]
        a.remove(poped)
        a.append(poped)
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')


