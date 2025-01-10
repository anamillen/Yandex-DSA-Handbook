"""
Ваша задача --- для m значений qi​ необходимо найти количество вхождений qi​ в K
"""

def num_of_occurences(length_li, li, key):
    """Returns the number of occurences of the key in the list li"""
    inf = -1
    sup = -1
    min_ind = 0
    max_ind = length_li - 1
    while max_ind>=min_ind:
        mid_ind = (min_ind + max_ind)//2
        if li[mid_ind]==key:
            inf = mid_ind
            max_ind = mid_ind - 1
        elif li[mid_ind]>key:
            sup = mid_ind
            max_ind = mid_ind - 1
        else:   # if li[mid_ind]<key
            min_ind = mid_ind + 1
    if sup!=-1:
        max_ind = sup
    else:
        max_ind = length_li - 1
    min_ind = inf
    while max_ind>=min_ind:
        mid_ind = (min_ind + max_ind)//2
        if li[mid_ind]==key:
            sup = mid_ind
            min_ind = mid_ind + 1
        elif li[mid_ind]>key:
            max_ind = mid_ind - 1
        else:   # if li[mid_ind]<key
            min_ind = mid_ind + 1
    if sup==-1 or inf == -1:
        return 0
    return sup - inf + 1
    # from here on out we have scanned the entire array (max_ind>min_ind)
    



# main program
n_elements = int(input())
li = [int(x) for x in input().split()]
n_keys = int(input())
keys = [int(x) for x in input().split()]
for i in range(n_keys):
    print(num_of_occurences(length_li=n_elements, li=li, key=keys[i]), end=" ")




