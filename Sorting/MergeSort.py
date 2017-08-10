# Merge sort
def merge(a, b):
    """Merge two lists sorted in descending order."""
    return [max(a, b).pop(0) for _ in a+b]

assert merge([], []) == []
assert merge([1], [0]) == [1,0]
assert merge([7,5,1], [2]) == [7,5,2,1]
print('All passed!')

merge([1,2,3],[4,5,6])