"""
Дана последовательность a из n целых чисел (возможно повторяющихся).

Ваша цель --- изменить описанный выше алгоритм RandomizedQuickSort так, 
чтобы даже при последовательностях с множеством повторяющихся элементов 
ожидаемое время выполнения стало O(n log(n)).
"""
import random

def separ_elems(seq, e):
    """Separates the list seq into 3 diff lists containing values
    - smaller than e
    - equal to e
    - bigger than e"""
    smaller = []
    equal = []
    bigger = []

    for curr in seq:

        if curr < e:
            smaller.append(curr)
        elif curr > e:
            bigger.append(curr)
        else:   # if curr == e then
            equal.append(curr)

    return smaller, equal, bigger

def modif_randomized_search(seq, n):
    """Randomized quick search modified to stay efficient with repeating elements"""
    res = []

    if n <= 1:
        res = list(seq)
    else:   # if the sequence has more than 1 element then
        rind = random.randint(0, n - 1)
        smaller, equal, bigger = separ_elems(seq, seq[rind])
        smaller = modif_randomized_search(smaller, len(smaller))
        bigger = modif_randomized_search(bigger, len(bigger))
        res = smaller + equal + bigger

    return res

# main program
n_elements = int(input())
seq = [int(x) for x in input().split()]
res = modif_randomized_search(seq, n_elements)
for e in res:
    print(e, end=" ")