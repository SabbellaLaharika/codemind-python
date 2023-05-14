n,s = int(input()),list(map(int, input().split()))
b = []
for i in s :
    if s.count(i) == 1 :
        b.append(i)
if len(b) != 0 :
    print(*b)
else :
    print(-1)