from collections import  Counter
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        key = str(args) + str(kwargs)
        helper.c[key] += 1
        return func(*args,**kwargs)

    helper.c = Counter()
    helper.calls = 0
    helper.__name__ = func.__name__
    return helper

def memorize(func):
    """
    This is for top-down approach of Dynamic programming. where repeated results are stored & referred later.
    """
    results = {}
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key not in results:
            results[key] = func(*args,**kwargs)
        return results[key]

    return wrapper

@call_counter
def EditDistRec(p,t):
    """ This is recursive solution without DP, highly inefficient """
    if p == "": return len(t)
    if t == "": return len(p)
    cost = 0 if p[-1] == t[-1] else 1

    res = min([EditDistRec(p[:-1],t)+1,
               EditDistRec(p,t[:-1])+1,
               EditDistRec(p[:-1],t[:-1])+cost])

    return res

print(EditDistRec("Python","Peithen"))
print(f"Function EditDistRec was called {str(EditDistRec.calls)} times ")
print(EditDistRec.c.most_common())


# THIS IS THE  TOP-DOWN DP APPROACH
@call_counter
@memorize
def ED_DP_TopDown(s,t):
    if s == "": return len(t)
    if t == "": return len(s)

    cost = 0 if s[-1] == t[-1] else 1

    res = min([ ED_DP_TopDown(s[:-1],t) + 1,
                ED_DP_TopDown(s,t[:-1]) + 1,
                ED_DP_TopDown(s[:-1],t[:-1]) + cost])
    return res

print("\n TOP DOWN DP APPROACH ")
print(ED_DP_TopDown("Python","Peithen"))
print(f"Function ED_DP_TopDown was called {str(ED_DP_TopDown.calls)} times ")
print(ED_DP_TopDown.c.most_common())



# THIS IS BOTTOM-UP APPROACH, WHICH IS ITERRATIVE APPROACH.
# https://www.python-course.eu/levenshtein_distance.php
@call_counter
def ED_DP_BottomUp(s,t):
    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # initialize base case
    for i in range(1,rows):
        dist[i][0] = i
    for i in range(1,cols):
        dist[0][i] = i

    for c in range(1,cols):
        for r in range(1,rows):
            cost = 0 if s[r-1] == t[c-1] else 1
            dist[r][c] = min(dist[r-1][c] + 1, # Deletion
                             dist[r][c-1] + 1, # Insertion
                             dist[r-1][c-1] + cost) # substitution
    # for debug info
    for row in range(len(dist)):
        print(dist[row])


    return dist[r][c]

print("\n BOTTOM-UP DP APPROACH ")
print(ED_DP_BottomUp("Cat","Cow"))
print(f"Function ED_DP_TopDown was called {str(ED_DP_BottomUp.calls)} times ")
print(ED_DP_BottomUp.c.most_common())

