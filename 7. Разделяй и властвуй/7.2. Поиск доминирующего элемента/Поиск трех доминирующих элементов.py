"""
Дана последовательность a из n целых чисел.

Ваша задача --- проверить, содержит ли данная последовательность элементы, которые встречаются более n/4 раз.
"""

# solves the problem using the majority vote algorithm

def find_3_candidates(len_li, li):
    can1, can2, can3 = None, None, None
    count1, count2, count3 = 0, 0, 0
    candidates = [None, None, None]
    counts = [0, 0, 0]
    for e in li:
        new_cand = False
        i = 0
        while not new_cand and i < 3:
            if counts[i] == 0 and e not in candidates:
                new_cand = True
                candidates[i] = e
            if e != candidates[i]:
                counts[i] -= 1
            else:   # if the current element is equal to the ith candidate
                counts[i] += 1
            i += 1
        # here we have either found a new candidate 
        # or have adjusted the votes for all current candidates (new_cand or i == 3)
        



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
        