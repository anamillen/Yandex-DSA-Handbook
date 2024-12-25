"""Реализуйте сортировку выбором."""

def selection_sort(li):
    """Sorts the list li using selection sort"""
    for i in range(len(li)):
        min_el_ind = i
        for j in range(i+1, len(li)):
            if li[j]<li[min_el_ind]:
                min_el_ind = j
        li[i], li[min_el_ind] = li[min_el_ind], li[i]

# main program
n = int(input())
nums = input().split()
li = []
for num in nums:
    li.append(int(num))
selection_sort(li)
for num in li:
    print(num, end=" ")


