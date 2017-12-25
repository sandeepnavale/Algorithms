# Find i & j, such that sum = a[i] + a[j]
def pairSum(arr,sum):
    h = {}
    for i in range(len(arr)):
        comp =  sum - arr[i]
        h[arr[i]] = i
#         print (i,arr[i],comp)
        if comp in h:
            return h[comp],i
    print(h)

if __name__ == '__main__':
    print(pairSum([2,3,4,5,6,7,8],7))
    print(pairSum([2,3,4,5,6,7,8],11))