"""Дано число n, необходимо найти последнюю цифру суммы Sn = 0​+F1​+F2​+…+Fn​."""

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
    else:   # if we have calculated the entire pisano period then
        period = len(mods)
        mod = mods[n%period]
    return mod


def last_digit_of_sum_Fn(n):
    """Returns the last digit of the sum of Fibonnaci's numbers up to Fn (included)"""
    # By induction we can prove that Sn = Fn+2 - 1, so we only need to calculate the last digit of Fn+2
    mod_of_fn2 = mod_of_big_Fn(n+2)
    last_digit = mod_of_fn2 - 1
    if last_digit==-1:  # treating special cases
        last_digit=9
    return last_digit

# main program
n = int(input())
print(last_digit_of_sum_Fn(n))

