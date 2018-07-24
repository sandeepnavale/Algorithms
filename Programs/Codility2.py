# /*
#  * Write a function that, given two strings S and T consisting of N and M characters, respectively,
#  * determines whether string T can be obtained from string S by at most one insertion or deletion
#  * of a character, or by swapping two adjacent charcters once. The function should return a string:
#  * - "INSERT c" if string T can be obtained from string S by inserting a single character "c";
#  * - "DELETE c" if string T can be obtained from string S by deleting a single character "c";
#  * - "SWAP c d" if string T can be obtained from String S by swapping two adjacent characters "c"
#  *    and "d" (these characters should be distinct and they should be in this order in string S);
#  * - "NOTHING" if no operation is needed (strings T and S are equal);
#  * - "IMPOSSIBLE" if none of the above works.
#  */
# https://gitlab.com/jakeprince/codility/blob/master/1.php

from unittest import TestCase

def Solution(s,t):
    n  = len(s)
    m  = len(t)

    sset = set(s)
    tset = set(t)
    diff = tset.difference(sset)
    if len(diff) == 1:
        print('DELETE c')

    print(tset.intersection(sset))
    print(tset.symmetric_difference(sset))
if __name__ == '__main__':
    Solution('ABC','ABX')
