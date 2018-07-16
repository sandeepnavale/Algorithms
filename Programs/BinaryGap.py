# Funtional method
def BinaryGap(n):
    i = n
    c = 0
    res = 0
    start_count = False
    while i:
        if i & 1:
            if start_count == False:
                start_count = True
            else :
                res = max(res,c)
            c = 0

        else:
            c += 1

        i = i >> 1
    return res

print(BinaryGap(529))
print(BinaryGap(32))
print(BinaryGap(15))
print(BinaryGap(6))



# Pythonic way
print('THIS IS PYTHONIC WAY')
print(len(max(format(529,'b').strip('0').split('1'))))

print(len(max(format(6,'b').strip('0').split('1'))))
