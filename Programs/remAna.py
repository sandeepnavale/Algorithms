# remove anagrams from an list of elements.

s = ['code', 'doce', 'ecod', 'framer', 'frame']


def funWithAnagrams(s):
    op = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if ''.join(sorted(s[i])) == ''.join(sorted(s[j])):
                op.append(s[i])
                op.append(s[j])

    for e in op:
        if e in s:
            s.remove(e)
    return s


print(funWithAnagrams(s))
