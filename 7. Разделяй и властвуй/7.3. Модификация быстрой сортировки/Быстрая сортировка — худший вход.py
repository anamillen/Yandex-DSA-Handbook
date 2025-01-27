"""
Данo число n. Вам необходимо построить массив, 
на котором алгоритм быстрой сортировки выполнит наибольшее количество рекурсивных вызовов.

При рассматриваемом отрезке l,r функции быстрой сортировки, 
считайте, что точка m выбирается по формуле m = ⌊( l + r ) / 2 ⌋
"""

def worst_case(seq, length):
    """Finds and returns the worst case scenario for the quick sort algorithm (time-wise)"""
    l = 0; r = length - 1
    small_e = 1; large_e = length
    place_largest = False

    def deepest_recursion_data(seq, l, r):
        """Returns a sequence of integers for which the quick sort algorithm 
        has the worst time complexity"""
        nonlocal small_e, large_e, place_largest
        if l <= r:

            m = (l + r) // 2
            place_largest = not place_largest
            if place_largest:
                seq[m] = large_e
                large_e -= 1
                deepest_recursion_data(seq, m + 1, r)
                deepest_recursion_data(seq, l, m - 1)
            else:   # if place_largest is false then
                seq[m] = small_e
                small_e += 1
                deepest_recursion_data(seq, l, m - 1)
                deepest_recursion_data(seq, m + 1, r)
        
    deepest_recursion_data(seq, l, r)

# main program
length = int(input())
seq = [0]*length
worst_case(seq, length)
for el in seq:
    print(el, end=" ")