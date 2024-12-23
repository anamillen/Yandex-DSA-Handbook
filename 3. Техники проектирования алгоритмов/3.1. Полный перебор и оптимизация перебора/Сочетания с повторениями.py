"""Выведите число сочетаний с повторением С‾(n,k)."""

def combinations_with_repetitions(n, k):
    """
    Returns the number of combinations of k elements out of n elements
    with repetitions allowed
    
    Examples:
    >>> combinations_with_repetitions(5, 3)
    35

    >>> combinations_with_repetitions(7, 2)
    28

    >>> combinations_with_repetitions(16, 2)
    136
    """
    c = 1
    r = n + k - 1
    for k_i in range(1, n+k):
        if k_i<=k:
            c/= k_i     # dividing by k!
        if k_i<=n-1:
            c/= k_i     # dividing by (n-1)!
        c*= k_i         # multiplying by (n+k-1)!
    return int(c)

# main
n, k = input().split()
print(combinations_with_repetitions(int(n), int(k)))