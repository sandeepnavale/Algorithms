# Merge sort
def merge(a, b):
    """Merge two lists sorted in descending order."""
    return [max(a, b).pop(0) for _ in a+b]

assert merge([], []) == []
assert merge([1], [0]) == [1,0]
assert merge([7,5,1], [2]) == [7,5,2,1]
print('All passed!')

merge([1,2,3],[4,5,6])



def mergesort2(seq):
    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort2(lft)
    if len(rgt) > 1: rgt = mergesort2(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

print('Another method',mergesort2([4,1,5,2,11]))

