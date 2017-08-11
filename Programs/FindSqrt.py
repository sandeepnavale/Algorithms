# Find square root of an number
# Uses Bin Search
import sys
def sqrt_search(x):
    start = 0
    end = sys.maxsize
    while start < end:
        mid = start + (end - start)/2
        midsqr = mid * mid
#         print("Start",start,"mid",mid,"End",end)
        if(x == midsqr):
            return mid
        elif x < midsqr:
            end = mid
        else:
            start = mid
    return start

print(sqrt_search(36))
print(sqrt_search(64))
print(sqrt_search(10000))
