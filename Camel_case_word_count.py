s = input()
cnt = 1
for i in range(1,len(s)) :
    if 65 <= ord(s[i]) <= 90 :
        cnt += 1
print(cnt)