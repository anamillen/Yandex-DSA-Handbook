"""Для двух чисел a и b найдите их наименьшее общее кратное."""\

def GCD(a, b):
    """Returns the greatest common divider of a and b"""
    if a!=0 and b!=0:
        gcd = GCD(b, a%b)     # as b>a%b and gcd(a-b, b)==gcd(a, b)
    else:   # if a or b are equal to 0 then (the end of euclidian algorithm)
        gcd = max(a, b)
    return gcd
    
def LCM(a,b):
    """Returns the least common multiple of a and b using their GCD"""
    prod = a*b
    gcd = GCD(max(a,b), min(a,b))
    return prod//gcd

# main program
a, b = [int(x) for x in input().split()]
print(LCM(a,b))