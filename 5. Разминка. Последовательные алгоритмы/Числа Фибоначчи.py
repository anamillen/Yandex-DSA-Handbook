"""Дано целое число n, необходимо вычислить n-е число Фибоначчи."""

def n_fibonacci(n):
    """Returns the value of the nth Fibonacci's number"""
    u_0 = 0
    u_1 = 1
    for _ in range(1, n):
        u_1, u_0 = u_1 + u_0, u_1
    return u_0 if n==0 else u_1

# main program
n = int(input())
print(n_fibonacci(n))


