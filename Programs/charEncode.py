def encode(s):
    s = list(s)
    i = 0
    k = 0
    while i < len(s):
        j = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            j += 1
            i += 1

        s[k] = s[i]
        k += 1
        s[k] = str(j)
        k += 1
        i += 1

    return ''.join(s)


print(encode('aaabbbccdddeaaaaaa'))


def encode2(s):
    a = list(s)
    i = 0
    op = []
    while i < len(a):
        j = 1
        while i + 1 < len(a) and a[i] == a[i + 1]:
            j += 1
            i += 1
        op.append(a[i])
        op.append(str(j))
        i += 1

    return ''.join(op)


print(encode2('aaabbbccdddeaaaaaa'))
