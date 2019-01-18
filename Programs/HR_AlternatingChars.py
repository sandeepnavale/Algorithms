# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
s = 'AABAAB'
length = len(s)
i = 0
c = 0
op = []
while i<length-1:
    if s[i]==s[i+1]:
        c += 1
    else:
        op.append(s[i])
    i+=1
op.append(s[i])
print(c,op)

