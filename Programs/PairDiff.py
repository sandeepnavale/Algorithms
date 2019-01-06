# https://www.hackerrank.com/challenges/pairs/problem

# best solution from HR;


def pairs(a, d):
    return len(set(a) & {x + d for x in a})


# print(pairs([1, 5, 3, 4, 2], 2))


# My solution.
# NOT PASSING ALL CASES
def pairs2(a, d):
    d1 = dict()
    for v in a:
        if v + d in a and v not in d1.keys() and v not in d1.values():
            d1[v] = v + d
        if v - d in a and v not in d1.keys() and v not in d1.values():
            d1[v] = v - d
    # print(d1)
    return len(d1)


# print(pairs2([1, 5, 3, 4, 2], 2))  #PASSING
# print(pairs2([1, 3, 5, 8, 6, 4, 2], 2))


def pairs3(a, d):
    s = set(a)
    count = 0
    for v in s:
        if v + d in s:
            count += 1
    return count


print(pairs3([1, 3, 5, 8, 6, 4, 2], 2))
