# String Permutation using manual method
# The idea is to one by one extract all elements, place them at first position and recur for remaining list.
# Python function to print permutations of a given list
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
for p in permutation(data):
    print(p)




# BEST METHOD USING ENUMBERATE
def perms(s):
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return result


print(perms('ABC'))
print(perms('XYZ'))


def permutations(string, step = 0):
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print ("".join(string))
    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [character for character in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)




if __name__ == '__main__':
    permutations('ABC')