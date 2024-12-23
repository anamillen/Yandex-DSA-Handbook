"""Выведите число сочетаний C(n,k)."""

def combinations(n, k):
    """Returns the number of combinations of k elements out of n elements
    
    Examples :
    >>> combinations(7, 2)
    21

    >>> combinations(23, 4)
    8855

    >>> combinations(3, 2)
    3
    """
    if k>n:
        # we ensure that we treat the impossible cases differently
        c = 0
    else:  # if the combinations value can be calculated then
        c = 1
        for k_i in range(1, n+1):
            c *= k_i        # multiplying by n!
            if k_i <= n-k:
                c /= k_i    # dividing by (n-k)!
            if k_i <= k:
                c /= k_i    # dividing by k!
    return int(c)

# main
n,k = input().split()
print(combinations(int(n), int(k)))
