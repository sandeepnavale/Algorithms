def selectionSortRec(seq, l):
    if l == 0: return
    maxEleIdx = l
    for i in range(l):
        if seq[i] > seq[maxEleIdx]:
            maxEleIdx = i

    seq[maxEleIdx], seq[l] = seq[l], seq[maxEleIdx]
    selectionSortRec(seq, l - 1)


a1 = [1, 22, 444, 5, 22, 55, 33]
# breakpoint()
print(a1)
selectionSortRec(a1, len(a1) - 1)
print(a1)

# Iterative version.
def selectionSort(seq):
    for l in range(len(seq)-1,0,-1):
        maxEleIdx = l
        for i in range(l):
            if seq[i] > seq[maxEleIdx]:
                maxEleIdx = i

        seq[maxEleIdx], seq[l] = seq[l], seq[maxEleIdx]
        

a = [1, 22, 444, 5, 22, 55, 33]
print('BEFORE: ',a)
selectionSort(a)
print('AFTER:',a)
