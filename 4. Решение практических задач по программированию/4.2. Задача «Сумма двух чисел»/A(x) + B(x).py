"""
Решите немного более сложную задачу.
Необходимо вычислить сумму двух многочленов
"""

def construct_poly(pwr):
    """Constructs and returns a polynomial of a degree pwr in form of a dictionary
    """
    poly = {}
    coeffs = input().split()
    for i in range(pwr+1):
        poly[i] = int(coeffs[pwr-i])
    return poly

def sum_polys(A, B):
    C = {}
    nA = len(A)
    nB = len(B)
    k = max(nA, nB)-1
    for i in range(k+1):
        if nA>nB:
            C[i] = A[i]
            if i in B:
                C[i] += B[i]
        else:   # if len(B)>=len(A)  
            C[i] = B[i]
            if i in A:
                C[i] += A[i]
    return k, C

# main program
A = construct_poly(int(input()))
B = construct_poly(int(input()))
k, C = sum_polys(A, B)
print(k)
for i in C:
    print(C[k-i], end=" ")