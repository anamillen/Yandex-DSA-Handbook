"""
Ваша задача --- проверить, содержит ли данная последовательность элемент, который встречается более половины раз.
"""

# solves the problem using Boyer-Moore Majority Vote algorithm
# time complexity is O(n)

def dominant_candidate(len_li, li):
    """Returns the dominant element of the list li if there's one,
    else returns None"""
    candidate = None
    count = 0

    for el in li:
        if count == 0:
            candidate = el
            count +=1
        else:   # if the element hasn't canceled out (count != 0)
            if el == candidate:
                count += 1
            else:   # if the current is not the candidate (el != candidate)
                count -= 1
    return candidate

def has_a_dominant(len_li, li):
    """Return 1 if the list li has a dominant element,
    0 otherwise"""
    answer = 0
    candidate = dominant_candidate(len_li, li)
    if candidate != None:
        count = li.count(candidate)
        if count > len_li // 2:
            answer = 1
    return answer
    
# main program
len_li = int(input())
li = [int(x) for x in input().split()]
print(has_a_dominant(len_li, li))