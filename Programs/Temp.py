def array_left_rotation(a, n, k):

    for i in range(n):
        poped = a.remove()
        a.insert(pop)
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

