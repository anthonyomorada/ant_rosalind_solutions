f = open('rosalind_revc.txt', 'r')
n = str(f.readlines())
print n
f.close

cDNA = ""
for i in n:
    if i == "A":
        cDNA += "T"
    elif i == "T":
        cDNA += "A"
    elif i == "C":
        cDNA += "G"
    elif i == "G":
        cDNA += "C"

cDNA = cDNA[::-1]
print(cDNA)


f = open('output.txt', 'a')
f.write(cDNA)

