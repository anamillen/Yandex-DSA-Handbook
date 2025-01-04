"""
Турист зашел в сувенирную лавку и нашел там много привлекательных вариантов подарков друзьям и родным. 
Всего в лавке n сувениров, стоимость i-го сувенира ci​ рублей.

Определите, какое наибольшее количество сувениров сможет купить турист, если он может потратить не более S рублей.
"""

def max_souvenirs(S, n, souvenirs):
    """Returns the max amount of souvenirs the tourist can buy without exceeding the sum S"""
    souvenirs = sorted(souvenirs)
    count = 0
    total = 0
    while total+souvenirs[count]<=S and count<n:
        total+=souvenirs[count]
        count+=1
    # from here on out it's either total+souvenirs[i]>S or i==n
    return count

# main program
n, S = [int(x) for x in input().split()]
souvenirs = []
for _ in range(n):
    souvenirs.append(int(input()))
print(max_souvenirs(S, n, souvenirs))

