def palindrome(string):
    """Check if input string (all lower-case characters) is a palindrome."""
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


assert palindrome('') == True
assert palindrome('a') == True
assert palindrome('ab') == False
assert palindrome('abba') == True
assert palindrome('redivider') == True
print('All passed!')
