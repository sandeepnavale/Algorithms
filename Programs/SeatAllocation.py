# Chapter 4: Python Algorithms.
M = [2, 2, 0, 5, 3, 5, 7, 4]


def naive_max_prem(M, A=None):
    """ This is an BF approach to find max permutation of seats.
    This is an quadratic complexity
    """
    if A is None:
        A = set(range(len(M)))  # Total number of persons
    if len(A) == 1: return A

    B = set(M[i] for i in A)  # Sets which are occupied.
    C = A - B  # Unused seats
    # print(A, M, B, C)
    if C:
        A.remove(C.pop())  # Remove unused person based on unused seat.
        return naive_max_prem(M, A)
    return A


print("Total Permutation (BF)", naive_max_prem(M))
