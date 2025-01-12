"""
Ваша задача --- для m значений qi​ необходимо найти количество вхождений qi​ в K
"""

def lower_bound(len_li, li, key):
    """
    Returns the smallest index i such that li[i] >= key.
    If all elements < key, returns len_li.
    """
    left = 0 
    right = len_li
    while left<right:
        mid = (left + right)//2
        if li[mid]>=key:
            right = mid
        else:   # if li[mid]<key
            left = mid + 1
    # from here on out left>=right
    return right

def upper_bound(len_li, li, key):
    """
    Returns the smallest index i such that li[i] > key.
    If all elements < key, returns len_li.
    """
    left = 0
    right = len_li
    while left<right:
        mid = (left + right)//2
        if li[mid]<=key:
            left = mid + 1
        else:   # if li[mid]>key
            right = mid
    # from here on out left>=right
    return right

def num_of_occurences(len_li, li, key):
    """Returns the number of occurences of the key in the list li"""
    first_occur = lower_bound(len_li, li, key)
    last_occur = upper_bound(len_li, li, key)
    return last_occur - first_occur
    
# main program
n_elements = int(input())
li = [int(x) for x in input().split()]
n_keys = int(input())
keys = [int(x) for x in input().split()]
for i in range(n_keys):
    print(num_of_occurences(len_li=n_elements, li=li, key=keys[i]), end=" ")




