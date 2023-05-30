s = input()
v = 'aeiou'
m = 0
for i in range(len(s)) :
    k = ''
    if s[i] in v :
        k += s[i]
        for j in range(i+1,len(s)) :
            if s[j] in v :
                k += s[j]
            else :
                break
        if m < len(k) :
            m = len(k)
print(m)