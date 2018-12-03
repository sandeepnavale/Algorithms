#
# Largest palindrome which is product of two n-digit numbers
# Given a value n, find out the largest palindrome number which is product of two n digit numbers.
#
# Examples :
#
# Input  : n = 2
# Output : 9009
# 9009 is the largest number which is product of two
# 2-digit numbers. 9009 = 91*99.
#
# Input : n = 3
# Output : 906609
def getPalindrome(n):
    s = '9' * n
    u = int(s)
    for i in range(u, 1, -1):
        for j in range(u, 1, -1):
            if (isPalindrome(i, j)):
                print(i, j, i * j)
                return


def isPalindrome(i, j):
    prod = i * j
    prod_s = str(prod)
    for i in range(len(prod_s) // 2):
        if prod_s[i] != prod_s[-(i + 1)]:
            return False
    return True


getPalindrome(5)
