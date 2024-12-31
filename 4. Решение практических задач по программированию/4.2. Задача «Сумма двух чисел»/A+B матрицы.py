"""Необходимо вычислить сумму двух матриц C = A + B."""

def sum_matrices(rows, cols, A, B):
    """Returns the sum of 2 matrices A and B of dimensions m x n"""
    summ = list(A)
    for row in range(rows):
        for col in range(cols):
            summ[row][col]+=B[row][col]
    return summ

def read_matrix(rows, cols):
    """Reads and returns a matrix as a 2d array"""
    matrix = []
    for _ in range(rows):
        inp = input().split()
        row = [int(x) for x in inp]
        matrix.append(row)
    return matrix

# main program
n, m = [int(x) for x in input().split()]
A = read_matrix(n, m)
B = read_matrix(n, m)
C = sum_matrices(n, m, A, B)

for row in C:
    for el in row:
        print(el, end=" ")
    print()