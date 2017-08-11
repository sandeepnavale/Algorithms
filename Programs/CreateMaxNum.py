# Create Maximum Number
# Given a number with n digits represented as a string, find maximum number with k digits, 0<k<n. Output result as a string.

def create_max(num, k):
    digits = list(num)
    drop = len(digits) - k
    stack = []
    for digit in digits:
        while drop and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)
    return ''.join(stack[:k])

num = '912583'
assert create_max(num, 1) == '9'
assert create_max(num, 2) == '98'
assert create_max(num, 3) == '983'
assert create_max(num, 4) == '9583'
assert create_max(num, 5) == '92583'
print('All passed!')