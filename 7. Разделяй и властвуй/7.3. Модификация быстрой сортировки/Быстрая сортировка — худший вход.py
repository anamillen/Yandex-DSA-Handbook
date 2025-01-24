"""
Данo число n. Вам необходимо построить массив, 
на котором алгоритм быстрой сортировки выполнит наибольшее количество рекурсивных вызовов.

При рассматриваемом отрезке l,r функции быстрой сортировки, 
считайте, что точка m выбирается по формуле m = ⌊( l + r ) / 2 ⌋
"""

def deepest_recursion_data(seq, e):
    """Returns a sequence of integers for which quick sort algorithm 
    has the worst time complexity"""
    len_seq = len(seq)
    m = len_seq // 2
    if len_seq == 1:
        seq[m] = e
    elif len_seq != 0:   # if the sequence has more than 1 element then
        seq[m] = e
        e = deepest_recursion_data(seq[:m], e - 1)
        deepest_recursion_data(seq[m+1:], e - 1)
    return e

n = int(input())
res = [0]*n
print(deepest_recursion_data(res, n))
print(res)