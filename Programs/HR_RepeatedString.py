""" Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
"""

def repeatedStrings(s,n):
    return s.count('a')*(n//len(s))+s[:n%len(s)].count('a')


s = 'aba'
n = 10
print(repeatedStrings(s,n))


s = 'a'
n = 1000000000000
print(repeatedStrings(s,n))

s = 'aba'
n = 1000000000000
print(repeatedStrings(s,n))
