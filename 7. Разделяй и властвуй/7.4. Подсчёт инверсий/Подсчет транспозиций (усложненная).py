"""
Дана перестановка p из n целых чисел. Необходимо вычислить, какое минимальное количество транспозиций требуется совершить, 
чтобы упорядочить элементы перестановки хорошо.

Будем говорить, что элементы перестановки упорядочены хорошо, если найдется такое число x от 1 до n, 
что перестановка имеет вид x, x+1, …, n, 1, 2, …, x−1.

Транспозиция -- это обмен соседних элементов перестановки p местами.
"""
def merge(left, right, splt, length):
    """Merges 2 lists left and right and returns the number of inversions effectuated"""
    
    srtd = []
    inversions = 0
    l = 0; r = 0

    while l < splt and r < length - splt:
        
        if left[l] <= right[r]:

            srtd.append(left[l])
            l += 1

        else:   # if right[r] < left[l]

            srtd.append(right[r])
            r += 1
            inversions = inversions + splt - l

    # here either l == splt or r ==  length (one of the array has ended)
    
    srtd += left[l:]
    srtd += right[r:]

    return srtd, inversions



def count_T(length, lst):

    min_T = length * (length - 1) / 2 + 1
    x = 1
    new = [ a - x if a >= x else a - x + length for a in lst]
    num_T = count_inversions(length, new)[1]
    
    while x <= length and min_T != 0:

        if num_T < min_T:

            min_T = num_T

        pos = lst.index(x)

        num_T = num_T + (length - 1) - 2*pos
        
        x += 1
    # here either we have tested all the x
    # or we have found a perfect solution with min_T = 0
    
    return min_T


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
inversions = count_T(length, lst)
print(inversions)