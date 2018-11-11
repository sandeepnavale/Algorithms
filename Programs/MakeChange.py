deno = [2000,200,100,50,5,1]

def makeChangeGreedy(n):
    notes = []
    for d in deno:
        while n >= d:
            n -= d
            notes.append(d)
    print(notes)
    return len(notes)

print(makeChangeGreedy(5551))

