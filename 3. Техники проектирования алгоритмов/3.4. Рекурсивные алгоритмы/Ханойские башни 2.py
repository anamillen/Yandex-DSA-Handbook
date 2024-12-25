"""
Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3. 
Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх. 
Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу. 
Диски в игре перемещаются по одному со стержня на стержень. 
Диск можно надеть на стержень, только если он пустой или верхний диск на нём большего размера, чем перемещаемый. 
Цель головоломки — перенести все диски со стержня 1 на стержень 3.

Немного изменим правила. Теперь головоломка состоит из четырех стержней, а цель головоломки — перенести все диски со стержня 1 на стержень 4. 
Найдите минимальное количество ходов, за которое можно решить головоломку.
"""

def moves_3pegs(n):
    """
    Return the minimal number of moves to solve the 3-peg Hanoi Tower
    problem with n disks.
    """
    return 2**n-1

def moves_4pegs(n):
    """
    Return minimal moves to solve the 4-peg Hanoi with n disks
    using the Frame–Stewart approach + memoization.
    """
    if n == 1:
        min_steps = 1
    else:   # if n!=1 (no more special cases)
        min_steps = float('inf')
        for k in range(1,n):
            total = 2*moves_4pegs(k)    # moving the k disk tower using 4 pegs
            total += moves_3pegs(n-k)   # solving for n-k disk tower and 3 pegs
            if total<min_steps:         # searching the minimum
                min_steps = total
    return min_steps

# main program
n = int(input())
print(moves_4pegs(n))
