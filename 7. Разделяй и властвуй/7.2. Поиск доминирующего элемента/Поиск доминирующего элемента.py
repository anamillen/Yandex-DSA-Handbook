"""
Ваша задача --- проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
"""
import random

# as it was stated in the paragraph if e is a dominating element => e is dominating in at least one of the halves
# here we will proceed in using contraposing (equivalent) statement:
# e isn't dominating in 1st half and e isn't dominating in 2nd half => e isn't a dominating element

def e_is_dominating(e, li):
    """Returns a boolean indicating if e is a dominating element in li"""
    count  = 0 
    len_li = len(li)
    dominating = 0

    if len_li == 1: 
        if li[0] == e:
            count = 1
            dominating = 1
    else:   # if the list has more than 1 element then
        splt = len_li//2
        first_half, _ = e_is_dominating(e, li[:splt])
        second_half, _ = e_is_dominating(e, li[splt:])
        count += first_half + second_half
        if count > len_li//2 :
            dominating = 1
    return count, dominating

def dom_elem_search(len_li, li):
    """Returns a boolean indicating if there are any dominating elements in a list li"""
    unique = list(set(li))
    len_unique = len(unique)
    has_dom = 0
    i = 0
    while has_dom == 0 and i < len_unique:
        _, has_dom = e_is_dominating(unique[i], li)
        i += 1
    # here we have either found 1 dominating number or have scanned all the elements
    return has_dom

# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(dom_elem_search(len_li, li))
