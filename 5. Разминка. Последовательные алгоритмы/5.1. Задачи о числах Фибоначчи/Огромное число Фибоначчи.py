"""Даны целые числа n и m, необходимо найти остаток от деления n-го числа Фибоначчи на m."""

def mod_of_big_Fn(n, divider=10):
    """Returns the modulo divider (10 by default) of n-th Fibonacci's number
    Algorithm suitable for very big values of n"""
    mods = []; i =0
    mod_0 = 0; mod_1 = 1
    while (i<=n and  not(mod_0==0 and mod_1==1)) or i==0:
        mods.append(mod_0)
        mod_1, mod_0, = (mod_0 + mod_1)%divider, mod_1%divider
        i+=1
    # from here on out it's:
    # i!=0 and ( i>n or (mod_0==0 and mod_1==1) )
    if i>n:
        mod = mods[n]
    else:
        period = len(mods)
        mod = mods[n%period]

    return mod

# main program
n, m = [int(x) for x in input().split()]
print(mod_of_big_Fn(n, m))
