"""Задано n отсортированных по неубыванию последовательностей.

Требуется найти отсортированную по неубыванию конкатенацию этих последовательностей."""

def merge_2(l1, l2):
    """Merges 2 sorted lists into one sorted list"""
    res = []
    while len(l1)>0 and len(l2)>0:
        if l1[0]<l2[0]:
            res.append(l1.pop(0))
        else:   # if l1[0]>=l2[0] (smallest element of l1 is bigger than smallest element of l2) then
            res.append(l2.pop(0))
    # from this point it's either len(l1)==0 or len(l2)==0
    res.extend(l1)
    res.extend(l2)
    return res

def merge_n(n, lists):
    """Merges n sorted lists into one sorted list"""
    res = []
    for i in range(n-1):
        res.extend(merge_2(lists[i], lists[i+1]))
    return res

# main program
n = int(input())
lists = []
for _ in range(n):
    k = int(input())
    nums = input().split()
    for i in range(k):
        nums[i] = int(nums[i])
    nums.sort()
    lists.append(nums)

if n==1:
    res = lists[0]
else:   # if there is more than 1 list in the list sequence then
    res = merge_n(n, lists)

for el in res:
    print(el, end=" ")
