"""Постройте разбиение Ломуто относительно первого числа."""

def lomutos_partition(li, pivot = 0):
    """Performs Lomuto's partition around pointer (0 by default)"""
    i = 0
    n = len(li)
    if n!=0:    # if the list is not empty then
        if pivot!=0:
            pivot_val = li[pivot]
            li[pivot], li[0] = li[0], li[pivot]
        for j in range(n):
            if li[j]<=pivot_val:
                li[j], li[i] = li[i], li[j] 
                i+=1
        li[i-1], li[0] = li[0], li[i-1]

# main program
li = []
n = int(input())
inp = input().split()
for el in inp:
    li.append(int(el))

lomutos_partition(li)
for el in li:
    print(el, end=" ")


