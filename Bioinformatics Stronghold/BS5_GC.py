string = open('rosalind_gc.txt', 'r').read().strip().split('>')
results = {}
for s in string:
    if len(s) > 0:
        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])
        results[label] = bases

def gc_content(s):
    n = len(s)
    m = 0
    for c in s:
        if c == 'G' or c == 'C':
            m += 1
    return 100 * (float(m) / n)

results = dict([(k, gc_content(v)) for k, v in results.iteritems()])

highest_k = None
highest_v = 0

for k, v in results.iteritems():
    if v > highest_v:
        highest_k = k
        highest_v = v

print highest_k
print highest_v

