"""Реализуйте сортировку слиянием."""

def merge(l1, l2):
    """Merges 2 sorted lists into one sorted list"""
    res = []
    i, j = 0, 0  # pointers for l1 and l2
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    # from this point it's either i==len(l1) or j==len(l2)
    res.extend(l1[i:])
    res.extend(l2[j:])
    return res

def merge_sort(li):
    """Performs recursive merge sort"""
    res = []
    n = len(li)
    if n==1:
        res = list(li)
    else:   # if the list li has more than 1 element then
        n_1st = n//2
        first = merge_sort(li[:n_1st])
        second = merge_sort(li[n_1st:])
        res = merge(first, second)

    return res

# main program
n = int(input())
nums = input().split()
li = []
for num in nums:
    li.append(int(num))
res =  merge_sort(li)
for el in res:
    print(el, end=" ")




