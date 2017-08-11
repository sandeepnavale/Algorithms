# Find all possible subsets of a list (or all possible sets of characters contained in a string).

def subsets(s):
    """Find all possible subsets of a list."""
    if not s:
        return [[]]
    res = []
    for sub in subsets(s[1:]):
        res.append(sub)
        res.append([s[0]]+sub)
    return res

assert subsets('') == [[]]
# please note, inputs 'abc' and ['a', 'b', 'c'] should be equivalent for your function
assert subsets('abc') == [[],['a'],['b'],['a','b'],['c'],['a','c'],['b','c'],['a','b','c']]
assert subsets(['a','b','c']) == [[],['a'],['b'],['a','b'],['c'],['a','c'],['b','c'],['a','b','c']]
print('All passed!')
