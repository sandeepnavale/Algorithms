"""Print a single integer denoting the number of characters you must delete
to make the two strings anagrams of each other."""


def number_needed(a, b):
    a, b = list(a), list(b)
    a_vals = list(a)
    for i in a_vals:
        if i in b:
            a.remove(i)
            b.remove(i)
    return len(a) + len(b)

x = input().strip()
y = input().strip()



print(number_needed(x, y))
