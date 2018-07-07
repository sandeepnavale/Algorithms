
def missingNum():
    lsum = 0
    n = int(input())
    lst =list(map(int,input().split()))
    for l in lst:
        lsum += l
        print(l,end=' ')
    nsum = n*(n+1)/2
    print(nsum-lsum)
        
if __name__ == '__main__':
    missingNum()
