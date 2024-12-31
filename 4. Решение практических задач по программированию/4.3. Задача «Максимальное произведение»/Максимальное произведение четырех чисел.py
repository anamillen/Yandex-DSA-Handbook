"""
Дана последовательность неотрицательных целых чисел а1,...,аn.

Вычислите max(ai * aj * ak * al) (i!=j!=k!=l)

Обратите внимание, что i, j, k и l должны быть разными, хотя в каких-то случаях можно наблюдать, что ai = aj​.
"""

def max_product_of_4(n,li):
    """Returns the max product of 3 integers of the list li"""
    li.sort()
    # these solutions are exhaustive (you can draw an x axis to see why)
    possible = [
        li[-1]*li[-2]*li[-3]*li[-4],
        li[0]*li[1]*li[-1]*li[-2],
        li[0]*li[1]*li[2]*li[3],

    ]
    # we will just find the max from all the possible solutions
    prod = max(possible)
    return prod

# main program
n = int(input())
li = [int(x) for x in input().split()]
print(max_product_of_4(n, li))
