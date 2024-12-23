"""Задано n n интервалов. 
Требуется найти максимальное количество взаимно непересекающихся интервалов.
Два интервала пересекаются, если они имеют хотя бы одну общую точку."""

# defining functions
def read_input(n):
    """Reads the given input and returns a 2d array containing
    left and right borders of n intervals"""
    intervs = []
    for _ in range(n):
        l, r = input().split()
        intervs.append([int(l), int(r)])
    return intervs

def find_champion(intervs):
    """Finds a champion interval [l,r] among intervals intervs
    Champion interval - is the interval where r is the smallest among r0, r1, ..."""
    champ_ind = 0; curr_min = intervs[0][1]
    for i in range(len(intervs)):
        if intervs[i][1]<=curr_min:
            curr_min = intervs[i][1]
            champ_ind = i
    return champ_ind

def del_interup(intervs, champ_ind):
    """Deletes the intervals which would interrupt the champion meeting"""
    l = intervs[champ_ind][0]
    r = intervs[champ_ind][1]
    i = 0
    while len(intervs)>0 and i<len(intervs):
        interv = intervs[i]
        if interv[0]<=r:
            intervs.pop(i)
        else:
            i+=1
    # from here it's either len(intervs)=0 or i=len(intervs)

def choose_intervals(intervs):
    """Chooses the optimal intervals for the meetings"""
    chosen_int = []
    while len(intervs)>0:
        champ_ind = find_champion(intervs)
        chosen_int.append(intervs[champ_ind])
        del_interup(intervs, champ_ind)
    return chosen_int


# main
n = int(input())
intervs = read_input(n)
chosen_int = choose_intervals(intervs)
print(len(chosen_int))