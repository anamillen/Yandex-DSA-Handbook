"""
Данo число n. Вам необходимо построить массив, 
на котором алгоритм быстрой сортировки выполнит наибольшее количество рекурсивных вызовов.

При рассматриваемом отрезке l,r функции быстрой сортировки, 
считайте, что точка m выбирается по формуле m = ⌊( l + r ) / 2 ⌋
"""

"""
def deepest_recursion_data(seq, start, end, e):
    \"""Returns a sequence of integers for which quick sort algorithm 
    has the worst time complexity\"""
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

"""

def worst_case(seq, length):
    """Finds and returns the worst case scenario for the quick sort algorithm (time-wise)"""
    l = 0; r = length - 1
    small_e = 1; large_e = length
    place_largest = True

    def deepest_recursion_data(seq, l, r):
        """Returns a sequence of integers for which the quick sort algorithm 
        has the worst time complexity"""
        nonlocal small_e, large_e, place_largest
        if l <= r:

            m = (l + r) // 2
            
            if place_largest:
                seq[m] = large_e
                large_e -= 1
            else:   # if place_largest is false then
                seq[m] = small_e
                small_e += 1
            
            place_largest = not place_largest
                
            deepest_recursion_data(seq, m + 1, r)
            deepest_recursion_data(seq, l, m - 1)
        
    deepest_recursion_data(seq, l, r)






length = int(input())
seq = [0]*length
worst_case(seq, length)
for el in seq:
    print(el, end=" ")