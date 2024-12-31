"""Задача-разминка: найдите сумму двух чисел."""

def summ(a,b):
    """Returns the sum of a and b"""
    return a+b

# main program
a, b = input().split()
print(summ(int(a), int(b)))