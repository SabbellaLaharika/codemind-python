s = input()
cnt = 0
n = len(s)
for i in range(n) :
    if s.count(s[i]) > 1 :
        cnt = 1
        break
if cnt == 0 :
    print("Unique Number")
else :
    print("Not Unique Number")