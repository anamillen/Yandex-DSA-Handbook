"""
Шахматы — очень интересная древнейшая настольная игра для двух игроков. 
Для решения этой задаче необязательно знать шахматные правила, но это может быть полезно.

В шахматах король — самая важная фигура. Король может сделать ход на любую из 8 соседних клеток шахматной доски. 
Соседними считаются клетки слева, справа, сверху, снизу и 4 по диагонали от рассматриваемой. 
В шахматной партии на игровом поле ровно один король каждого цвета.

Рассмотри задачу-головоломку о нескольких шахматных королях на доске произвольного размера.

Рассмотрим шахматную доску с r строками и c столбцами. 
Найдите наибольшее количество королей, которых можно разместить на доске r×c, с выполнение следующих условий:

    В любой клетке на доске может находиться не более одного короля.
    У любого короля есть по крайней мере один возможный ход на свободную клетку на доске.

"""

def maxkings(rows, cols):
    """Returns the maximum number of kings which can be placed
    on a rows x cols chessboard"""
    spare_cells = 0
    # we need to minimize the amount of spare cells, the best constrution for that is when
    # 8 kings share only 1 spare cell, therefore, 
    # for each 3×3 block (stepping by 3 in both dimensions), we place exactly one empty cell
    # this ensures that every king in that 3×3 block has at least one free neighboring square
    for row in range(0, rows, 3):
        for col in range(0, cols, 3):
            spare_cells+=1
    # we substract the spare cells from the total area of the board
    answer = (rows*cols) - spare_cells
    return answer

# main program
rows, cols = [int(x) for x in input().split()]
print(maxkings(rows=rows, cols=cols))


