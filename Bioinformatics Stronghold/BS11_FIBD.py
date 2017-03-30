n,m = map(int, open('rosalind_fibd.txt', 'r').read().split())
print n
print m

x = [0] * (n)

def F(n):
    if n < 0:
        return 0
    elif n < 3:
        return 1
    else:
        if x[n-1] != 0:
            return x[n-1]
        else:
            x[n-2] = F(n-1)
            return F(n-1) + F(n-2) - F(n-1-m)


results = F(n)
print results
