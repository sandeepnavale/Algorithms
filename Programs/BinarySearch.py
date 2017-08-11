def find_in_sorted(nums, target):
    """Binary search."""
    start, end = 0, len(nums)-1
    while start < end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1

assert find_in_sorted([], 0) == -1
assert find_in_sorted([1,2,3], 0) == -1
assert find_in_sorted([1,2,3], 2) == 1
assert find_in_sorted([1,2,2,2,2,2,3], 2) in range(1, 6)
assert find_in_sorted([1,2,3,4,6,7,8,12,13,16], 12) == 7
print('All passed!')