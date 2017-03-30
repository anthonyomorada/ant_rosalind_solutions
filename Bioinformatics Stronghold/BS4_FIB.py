f = open('rosalind_fib.txt', 'r')
n, k = map(int, f.read().strip().split())
print n, k
f.close

rabbits = [0,1]
for i in xrange(n-1):
    rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

print rabbits[n % 2]

f = open('output.txt', 'w')
f.write(str(rabbits[n % 2]))
f.close

