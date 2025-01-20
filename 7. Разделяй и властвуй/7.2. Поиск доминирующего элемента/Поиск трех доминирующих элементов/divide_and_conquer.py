"""
Дана последовательность a из n целых чисел.

Ваша задача --- проверить, содержит ли данная последовательность элементы, которые встречаются более n/4 раз.
"""

# solves the problem using a divide and conquer algorithm

def find_candidates(len_li, li):
    """Returns 3 dominating candidates"""
    if len_li == 1:
        doms = [li[0]]

    else:   # if the list has more than 1 element then
        doms = []
        splt = len_li // 2
        left_cands = find_candidates(splt, li[:splt])
        right_cands = find_candidates(len_li - splt, li[splt:])
        cands = list(set(left_cands + right_cands))

        for cand in cands:
            if e_dominates(cand, li, len_li):
                doms.append(cand)
        
    return doms

def e_dominates(el, li, len_li):
    dominates = False
    if li.count(el)> len_li // 4:
        dominates = True

    return dominates

def has_3_dominants(len_li, li):
    """Returns 1 if the number of dominants in the list exactly 3, 0 otherwise"""
    ans = 0
    doms = find_candidates(len_li, li)
    if len(doms) == 3:
        ans = 1

    return ans

# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(has_3_dominants(len_li, li))
        