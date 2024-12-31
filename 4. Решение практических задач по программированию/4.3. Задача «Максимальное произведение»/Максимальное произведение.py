"""
Дана последовательность неотрицательных целых чисел а1,...,аn.

Вычислите max(ai * aj) (i!=j)

Обратите внимание, что i и j должны быть разными, хотя в каких-то случаях можно наблюдать, что ai = aj​.
"""

def max_product(n, li):
    """Returns the max product of 2 different elements of the list li"""
    j_ind = 0
    for i in range(1, n):
        if li[i]>li[j_ind]:
            j_ind = i
    j = li.pop(j_ind)
    i_ind = 0
    for i in range(1, n-1):
        if li[i]>li[i_ind]:
            i_ind = i
    i = li.pop(i_ind)
    return j*i

# main program
n = int(input())
li = [int(x) for x in input().split()]
print(max_product(n, li))