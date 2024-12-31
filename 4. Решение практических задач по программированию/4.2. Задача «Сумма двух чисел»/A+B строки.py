"""Необходимо вычислить "кривую" сумму двух строк A и B одинаковой длины."""

def wiggly_sum(n, A, B):
    """Returns a string which resembles a sum of two strings A and B as follows:
    abc + def = adbecf"""
    res = ""
    for i in range(n):
        res+=A[i]+B[i]
    return res

# main program
n = int(input())
A = input()
B = input()
print(wiggly_sum(n, A, B))