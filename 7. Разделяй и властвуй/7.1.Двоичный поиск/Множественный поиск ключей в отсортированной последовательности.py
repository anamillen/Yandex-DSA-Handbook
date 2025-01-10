"""
Ваша задача --- для m значений qi​ необходимо проверить, входит ли qi​ в K.
"""

def binary_search(length, li, q):
    """Returns the index of the element q in li"""
    min_i = 0
    max_i = length - 1
    ind = -1
    while min_i <= max_i and ind==-1:
        mid_i = (min_i + max_i)//2
        if li[mid_i] == q:
            ind = mid_i
        elif li[mid_i]>q:
            max_i = mid_i - 1
        else:   # if li[mid_i]<q
            min_i = mid_i + 1
    # from here on out we have searched the entire list (max_i<min_i)
    # or have found the element we searched for (ind!=-1)
    return ind

# main program
length = int(input())
li = [int(x) for x in input().split()]
num_q = int(input())
qs = [int(x) for x in input().split()]
for i in range(num_q):
    print(binary_search(length, li, qs[i]))