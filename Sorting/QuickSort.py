def quicksort(nums, start=0, end=None):
    """Quicksort using last element as pivot."""
    def partition(nums, start, end):
        pindex = start
        pivot = end
        for i in range(start, end):
            if nums[i] <= nums[pivot]:
                nums[i], nums[pindex] = nums[pindex], nums[i]
                pindex += 1
        nums[pindex], nums[pivot] = nums[pivot], nums[pindex]
        return pindex

    if not end:
        end = len(nums) - 1
    if start >= end:
        return None
    pivot = partition(nums, start, end)
    quicksort(nums, start, pivot - 1)
    quicksort(nums, pivot + 1, end)


a = [2, 9, 2, 3, 5, 8, 1]
quicksort(a)
assert a == [1, 2, 2, 3, 5, 8, 9]
print('All passed!')