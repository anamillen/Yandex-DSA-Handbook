"""
Дан массив a из n целых чисел. Необходимо вычислить количество полуинверсий в этом массиве. 
Полуинверсия -- это такая пара индексов i,j, что i < j  и ai ​≥ aj​.
"""

def merge(left, right, splt, length):
    """Merges 2 lists left and right and returns the number of inversions effectuated"""
    
    srtd = []
    inversions = 0
    l = 0; r = 0

    while l < splt and r < length - splt:
        
        if left[l] < right[r]:

            srtd.append(left[l])
            l += 1

        else:   # if right[r] <= left[l]

            srtd.append(right[r])
            r += 1
            inversions = inversions + splt - l

    # here either l == splt or r ==  length (one of the array has ended)
    
    srtd += left[l:]
    srtd += right[r:]

    return srtd, inversions


def count_inversions(length, lst):
    """Returns the number of inversions in lst"""

    inversions = 0
    srtd = lst

    if length > 1:
        
        splt = length // 2
        left, left_inv = count_inversions(splt, lst[:splt])
        right, right_inv = count_inversions(length - splt, lst[splt:])
        srtd, splt_inv = merge(left, right, splt, length)
        inversions = left_inv + right_inv + splt_inv 

    return srtd, inversions

# main program
length = int(input())
lst = [int(x) for x in input().split()]
inversions = count_inversions(length, lst)[1]
print(inversions)