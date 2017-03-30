x = open('rosalind_grph.txt', 'r').read().strip().split('>')


print x

r = []
for s in x:
    if len(s):
        p = s.split()
        k = p[0]
        v = ''.join(p[1:])
        r.append((k,v))

results = []
for k1, v1 in r:
    for k2, v2 in r:
        if k1  != k2 and v1.endswith(v2[:3]):
            results.append((k1, k2))

for i in results:
    print i[0], i[1]
