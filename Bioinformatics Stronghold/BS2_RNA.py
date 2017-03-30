f = open('input.txt', 'r')
n = str(f.readlines())
print n
f.close

RNA = ""
for i in n:
    if i == "T":
        RNA += "U"
    else:
        RNA += i

print(RNA)


f = open('output.txt', 'a')
f.write(RNA)

