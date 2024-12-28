"""Постройте разбиение Ломуто относительно первого числа."""

def lomutos_partition(li, pivot = 0):
    """Performs Lomuto's partition around pointer (0 by default)"""
    i = pivot
    n = len(li)
    for j in range(n):
        if li[j]<=li[pivot]:
            li[j], li[i] = li[i], li[j] 
            i+=1
    if n!=0:
        li[pivot], li[i-1] = li[i-1], li[pivot]    

# main program
li = []
n = int(input())
inp = input().split()
for el in inp:
    li.append(int(el))

lomutos_partition(li)
for el in li:
    print(el, end=" ")


