"""
Данo число n. Вам необходимо построить массив, 
на котором алгоритм быстрой сортировки выполнит наибольшее количество рекурсивных вызовов.

При рассматриваемом отрезке l,r функции быстрой сортировки, 
считайте, что точка m выбирается по формуле m = ⌊( l + r ) / 2 ⌋
"""

def deepest_recursion_data(seq, start, end, e):
    """Returns a sequence of integers for which quick sort algorithm 
    has the worst time complexity"""
    len_seq = (end - start) + 1
    m = (start + end) // 2
    if len_seq == 1:
        seq[m] = e
    elif len_seq == 0:   
        e += 1
    else: # if the sequence has more than 1 element then
        seq[m] = e
        e = deepest_recursion_data(seq, start, m - 1, e - 1)
        e = deepest_recursion_data(seq, m+1, end, e - 1)
    return e

n = int(input())
res = [0]*n
deepest_recursion_data(res, 0, n-1, n)
for el in res:
    print(el, end=" ")