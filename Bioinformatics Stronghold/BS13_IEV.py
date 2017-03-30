a,b,c,d,e,f = map(int, open('rosalind_iev.txt', 'r').read().split())


a *= 2
b *= 2
c *= 2
d *= 1.5
e *= 1
f *= 0

total = a + b + c + d + e + f
print total
