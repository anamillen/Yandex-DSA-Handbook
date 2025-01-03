"""Для двух чисел a и b найдите их наибольший общий делитель."""

def GCD(a, b):
    """Returns the greatest common divider of a and b"""
    if a!=0 and b!=0:
        gcd = GCD(b, a%b)     # as b>a%b and gcd(a-b, b)==gcd(a, b)
    else:   # if a or b are equal to 0 then (the end of euclidian algorithm)
        gcd = max(a, b)
    return gcd

# main program
a, b = [int(x) for x in input().split()]
gcd = GCD(max(a,b), min(a,b))
print(gcd)