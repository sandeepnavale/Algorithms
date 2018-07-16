# ﻿Generate the BIT permutation.

def appendAtBegin(x, R):
    return [x + ele for ele in R]


def GenBitString(n):
    if n == 0: return []
    if n == 1:
        return ["0", "1"]
    else:
        return (appendAtBegin("0", GenBitString(n - 1)) +
                appendAtBegin("1", GenBitString(n - 1)))


print("\n 2 Bits", GenBitString(2))
print("\n 3 Bits", GenBitString(3))
print("\n 4 Bits", GenBitString(4))