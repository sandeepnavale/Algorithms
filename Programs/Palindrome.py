def palindrome(string):
    """Check if input string (all lower-case characters) is a palindrome."""
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

def palindrome2(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))


assert palindrome('') == True
assert palindrome('a') == True
assert palindrome('ab') == False
assert palindrome('abba') == True
assert palindrome('redivider') == True
print('All passed!')


assert palindrome2('') == True
assert palindrome2('a') == True
assert palindrome2('ab') == False
assert palindrome2('abba') == True
assert palindrome2('redivider') == True
print('All passed!')


a = 'abcdef'
for i in range(0,len(a)):
    print(i,~i)
    print(a[i],a[~i])
