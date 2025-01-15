"""
Дана последовательность a из n целых чисел.

Ваша задача --- проверить, содержит ли данная последовательность элементы, которые встречаются более n/4 раз.
"""

def has_3_dominants(len_li, li):
    """Returns 1 if the list li has 3 dominant elements,
    0 otherwise"""
    counter = {}
    cands = []
    for el in li:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    for num in counter:
        if counter[num] > len_li // 4:
            cands.append(num)
    if len(cands)==3:
        return 1
    else:
        return 0

# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(has_3_dominants(len_li, li))
        