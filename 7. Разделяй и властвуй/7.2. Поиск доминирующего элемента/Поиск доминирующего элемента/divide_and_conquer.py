"""
Ваша задача --- проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
"""
# solves the problem using divide-and-conquer approach
# time complexity is O(n log(n))

def dominant_candidate(len_li, li):
    """Returns the dominant element of the list li if there's one,
    else returns None"""
    candidate = None
    if len_li==1:
        candidate = li[0]
    else:   # if the list has more than 1 element then
        mid = len_li//2
        left_cand = dominant_candidate(mid, li[:mid])
        right_cand = dominant_candidate(len_li -  mid, li[mid:])

        if left_cand != None:
            left_count = li.count(left_cand)
            if left_count > mid:
                candidate = left_cand                
        
        if right_cand != None:
            right_count = li.count(right_cand)
            if right_count > mid:
                candidate = right_cand

    return candidate

def has_a_dominant(len_li, li):
    """Return 1 if the list li has a dominant element,
    0 otherwise"""
    answer = 0
    candidate = dominant_candidate(len_li, li)
    count = li.count(candidate)
    if count > len_li // 2:
        answer = 1
    return answer
    
# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(has_a_dominant(len_li, li))