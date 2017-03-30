import os
path = 'C:\Users\Anthony\Documents\GitHub\Rosalind'
print os.getcwd()
os.chdir(path)
print os.getcwd()

f = open('input.txt', 'r')
lines = f.readlines()[1::2]
print lines
f.close

f = open('input.txt', 'a')
f.write("\n\n")
for i in lines:
  f.write(str(i))
f.close()


