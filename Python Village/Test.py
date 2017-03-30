import os
path = 'C:\Users\Anthony\Documents\GitHub\Rosalind'
print os.getcwd()
os.chdir(path)
print os.getcwd()

f = open('input.txt', 'r')
print f.readlines()[1::2]
f.close()
