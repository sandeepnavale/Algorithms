from random import randint
def quicksort(seq):
    if len(seq) <= 1: return seq # Base case
    lo, pi, hi = partition(seq) # pi is in its place
    return quicksort(lo) + [pi] + quicksort(hi) # Sort lo and hi separately

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi
    # Pick and remove the pivot # All the small elements
    # All the large ones
    # pi is "in the right place"

print (quicksort([10,22,3,445,6,1,100]))
#print (quicksort([111,22,43,455645,6,1,1400]))
print (quicksort(["","sandeep","nls","abc","az",'a']))

a = [randint(10,100) for i in range(10)]
print("Input List ",a)
print("Sorted List ",quicksort(a))


