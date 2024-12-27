"""Задано n отсортированных по неубыванию последовательностей.

Требуется найти отсортированную по неубыванию конкатенацию этих последовательностей."""

def merge_2(l1, l2):
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

def merge_n(n, lists):
    """Merges n sorted lists into one sorted list"""
    res = lists[0]
    for i in range(1, n):
        res = merge_2(res, lists[i])
    return res

# main program
n = int(input())
lists = []
for _ in range(n):
    k = int(input())
    nums = input().split()
    for i in range(k):
        nums[i] = int(nums[i])
    lists.append(nums)

res = merge_n(n, lists)

for el in res:
    print(el, end=" ")

