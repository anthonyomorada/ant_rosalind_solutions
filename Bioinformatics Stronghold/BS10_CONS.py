x = open('rosalind_cons.txt', 'r').read().strip()
dna = x.split()
matrix =[]
txt = ''
clr = ''
for i in range(len(dna)):
    if dna[i][0] != '>':
        txt += dna[i]
    elif dna[i][0] == '>':
        matrix.append(txt)
        txt = clr

matrix.append(txt)
matrix.remove('')
        

fill = [0]*len(matrix[0])
results = {
    'A': fill[:],
    'C': fill[:],
    'G': fill[:],
    'T': fill[:],
    }

for s in matrix:
        for i, c in enumerate(s):
            results[c][i] += 1


seq = ''
key = results.keys()
for i in range(len(results[key[0]])):
    max_fill = 0
    max_key = ''
    for k in key:
        x = results[k][i]
        if x > max_fill:
            max_fill = x
            max_key = k
    seq += max_key

print seq
for i in sorted(results.iterkeys()):
        print "%s: %s" % (i, ' '.join(map(str, results[i])))





