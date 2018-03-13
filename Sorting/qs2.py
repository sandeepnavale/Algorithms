def qs(a):
    if (len(a)<=1 ): return a
    ls, pi, rs = parition(a)
    return qs(ls)+[pi]+qs(rs)

def parition(a):
    pivot,rest = a[0],a[1:]
    ls = [x for x in rest if x<pivot]
    rs = [y for y in rest if y>pivot]
    return ls,pivot,rs

qs([1,3,55,6,2])
qs([111,3,1,55,222])
