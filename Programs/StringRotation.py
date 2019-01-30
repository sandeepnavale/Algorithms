# 1.9 problem of Cracking the code interview.
# String Rotation:Assumeyou have a method isSubstring which checks if one word is a substring of another.
# Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring
# (e.g.,"waterbottle" is a rotation of"erbottlewat").

# My solution
def stringRotation(s1, s2):
    """
    finds the rotation of s1 & s2.
    :param s1:
    :param s2:
    :return:
    """
    a1 = list(s1)
    a2 = list(s2)
    count = 0
    while a1 != a2:
        a2.insert(0,a2.pop())
        count += 1
    return count


print(stringRotation('waterbottle', 'rbottlewate'))


# Actual solution.
# def stringRotationUsingSubstring(s1,s2):
#     return isSubtring(s1+s1, s2)
# S2 is always the substring os s1+s1,

