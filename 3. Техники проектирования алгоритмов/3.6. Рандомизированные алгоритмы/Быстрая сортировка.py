"""Реализуйте QuickSort."""
import random

def lomutos_partition(li, pivot = 0):
    """Performs Lomuto's partition around pointer (0 by default)"""
    i = 0
    n = len(li)
    if n!=0:    # if the list is not empty then
        pivot_val = li[pivot]
        if pivot!=0:
            li[pivot], li[0] = li[0], li[pivot]
        for j in range(n):
            if li[j]<=pivot_val:
                li[j], li[i] = li[i], li[j] 
                i+=1
        li[i-1], li[0] = li[0], li[i-1]
    return i-1

def quick_sort(li):
    """Sorts the list li by using QuickSort"""
    n = len(li)
    res = []
    if n<=1:
        res = li
    else:   # if the list li has more than 1 element then
        pivot = random.randint(0, n-1)
        pivot = lomutos_partition(li, pivot)
        first = quick_sort(li[:pivot])
        second = quick_sort(li[pivot:])
        res = first + second
    return res

# main program
li = []
n = int(input())
inp = input().split()
for el in inp:
    li.append(int(el))

li = quick_sort(li)
for el in li:
    print(el, end=" ")