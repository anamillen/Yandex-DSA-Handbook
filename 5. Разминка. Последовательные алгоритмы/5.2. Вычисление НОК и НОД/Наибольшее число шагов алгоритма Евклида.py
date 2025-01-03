"""Дано число n, найдите значения a и b (0≤a,b≤n), для которых количество вызовов функции GCD будет наибольшим."""

# here we will have to apply the next reasoning:

# when a/b is large, then a mod b decreases very rapidly
# so we're getting closer to 1 and 0 quicker
# as we need to find the pair for which the algorithm is most inefficient
# we will look for such numbers where a/b is as close to 1 as possible
# without actually being 1...

# as Fn/Fn-1 is always getting closer and closer to 1.618 then Fibonacci numbers will do

def max_fibs_up_to_n(n):
    """Returns the 2 biggest Fibonacci's numbers up to n"""
    fibs = [0, 1]
    while fibs[0]+fibs[1]<=n:
        fibs[0], fibs[1] = fibs[1], fibs[0]+fibs[1]
    # from here on out fibs[0]+fibs[1]>n
    return fibs

# main program
n = int(input())
a, b = max_fibs_up_to_n(n)
print(a, b)
