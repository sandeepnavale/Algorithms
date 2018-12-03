a = [4, 1, -5, 5, 4, 1, -1, 5]

def kadanes(a):
    maxtill, bestmax = 0, 0

    for i in range(len(a)):
        maxtill = max(a[i], maxtill + a[i])
        bestmax = max(maxtill, bestmax)
    return bestmax


print(kadanes(a))
