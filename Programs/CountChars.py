# Count char's without using any extra data strucutre.

from collections import defaultdict


# with Data Structure.
def countChars(s):
    dd = defaultdict(int)
    for c in s:
        if dd[c]:
            print(f'{c} is already present in {s} ')
            return False
        else:
            dd[c] += 1

    return True


# countChars('ABCDAEF')


def countCharsWithOutDS(s):
    for i, c in enumerate(s):
        if c in s[:i] + s[i + 1:]:
            print(f'{c} is already present in {s[:i] + s[i + 1:]}')


countCharsWithOutDS('ABCDEBF')

def countCharsWithOutDS2(s):
    s1 = sorted(s)
    for i in range(len(s1)-1):
        if s1[i] == s1[i+1]:
            print(f'{s1[i]} is present in {s1}')


countCharsWithOutDS2('ABCDEBFA')
