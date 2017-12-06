n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
#         import ipdb; ipdb.set_trace()

        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print (l)