"""Головоломка <<Ханойские башни>> состоит из трёх стержней, пронумеруем их слева направо: 1, 2 и 3. 
Также в головоломке используется стопка дисков с отверстием посередине. Радиус дисков уменьшается снизу вверх. 
Изначально диски расположены на левом стержне (стержень 1), самый большой диск находится внизу. 
Диски в игре перемещаются по одному со стержня на стержень. Диск можно надеть на стержень, 
только если он пустой или верхний диск на нём большего размера, чем перемещаемый. 
Цель головоломки — перенести все диски со стержня 1 на стержень 3.

Требуется найти последовательность ходов, которая решает головоломку <<Ханойские башни>>."""

def hanoi_towers(n, init, fin):
    """The recursive algorithm solving the Hanoi Towers problem
    Prints out the steps to effectuate to solve the problem"""
    if n==1:
        print(init,fin)
    else:   # if there's more than 1 disk on the current peg then
        unused = 6 - init - fin # as we consider a classical problem with 3 pegs
        hanoi_towers(n-1, init, unused)
        print(init, fin)
        hanoi_towers(n-1, unused, fin)
    
# main program 
n = int(input())
print(2**n-1)
hanoi_towers(n, 1, 3)