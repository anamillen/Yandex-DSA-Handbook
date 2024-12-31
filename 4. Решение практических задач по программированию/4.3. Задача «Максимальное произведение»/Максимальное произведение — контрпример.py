"""Определите, можно ли построить такой пример входных данных, чтобы количество сравнений в алгоритме MaxPairwiseProduct было больше 1.5n."""

"""
We will examine the algorithm and will count the number n of comparisons:

MaxPairwiseProduct(A[1..n]):
    m1 = A[1]
    m2 = A[2]
    if m2 > m1:    # +1 comparison 
        swap(m1, m2)

    for i from 3 to n:  # the loop executes n-3+1 = n-2 times
        if A[i] > m1:   # +1 comparison
            m2 = m1
            m1 = A[i]
        else:
            if A[i] > m2:   # +1 comparison (if else is satisfied)
                m2 = A[i]
    return m1 * m2

# we can see that by the end of execution of our function the mas number of caomparisons is:
# 1 + 2*(n-2) = 1 + 2*n - 4 = 2*n - 3
# from that we can conclude that we need the next inequation to be satisfied:
# 2*n - 3 > 1.5*n <=> 4*n - 6 > 3*n <=> 
# n > 6

# to achieve the max number of comparisons we will need
# A[i] <= m1 satisfied for as many i as possible as well
"""

# main program
n = int(input())
if n>6:
    print("Yes")
    for i in range(n, 0, -1):
        print(i, end=" ")
else:   # if n<=6
    print("No")
    