"""
Дано число n, необходимо найти последнюю цифру n-го числа Фибоначчи.

Числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением. 
Однако в данной задаче эту проблему можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи. 
Если 0≤a, b≤9 — это последние цифры чисел Fi​ и Fi+1​ соответственно, то (a+b)mod10  — это последняя цифра числа Fi+2​"""

def mod_of_Fn(n, divider=10):
    """Returns the modulo divider (10 by default) of n-th Fibonacci's number"""
    mod_0 = 0
    mod_1 = 1
    for _ in range(n):
        mod_1, mod_0, = (mod_0 + mod_1)%divider, mod_1%divider
    return mod_0

# main program
n = int(input())
print(mod_of_Fn(n))

