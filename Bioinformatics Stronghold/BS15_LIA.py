k, N = map(int, open('rosalind_lia.txt', 'r').read().strip().split())
print k
print N

import math

def binomial(x,y):
    if y == x:
        return 1
    elif y == 1:
        return x
    elif y > x:
        return 0
    else:
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x-y)
        div = a // (b * c)
        return div

def P(n,k):
    return binomial(2**k,n) * 0.25**n * 0.75**(2**k - n)


def problem(k,N):
    return 1-sum([P(n,k) for n in range(N)])

print problem(k,N)
