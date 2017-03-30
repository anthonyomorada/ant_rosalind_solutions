s, t = map(str, open('rosalind_subs.txt', 'r').read().strip().split())
print s
print t
for i in range(len(s)):
    if s[i] == t[0]:
        if t == s[i:i+len(t)]:
            print i+1,
            
            
