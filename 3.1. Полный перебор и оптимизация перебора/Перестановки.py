"""Выведите число перестановок P(n)."""

def permutations(n):
    """
    Returns the number of permutations of an integer n
    
    Parameters :
    -n (int) : an integer for which the number of permutations is counted
    
    Returns :
    - p (int) : number of permutations of n

    Examples:
    >>> permutations(3)
    6

    >>> permutations(0)
    1
    """
    p = 1
    for k in range(1,n+1):
        p *= k
    return int(p)

# main 
n = int(input())
print(permutations(n))