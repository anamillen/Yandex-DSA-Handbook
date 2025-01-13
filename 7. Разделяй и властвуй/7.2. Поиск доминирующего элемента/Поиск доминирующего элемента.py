"""
Ваша задача --- проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
"""

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
    has_dom = 0
    i = 0
    dupes = []
    while has_dom == 0 and i < len_li:
        if li[i] not in dupes:
            _, has_dom = e_is_dominating(li[i], li)
            dupes.append(li[i])
        i += 1
    # here we have either found 1 dominating number or have scanned all the elements
    return has_dom

# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(dom_elem_search(len_li, li))