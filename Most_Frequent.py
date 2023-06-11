n = int(input())
l = list(map(int, input().split()))
cnt = []
for i in l :
    if i not in cnt :
        cnt.append(l.count(i))
mx = []
for i in l :
    if l.count(i) == max(cnt) :
        mx.append(i)
print(min(mx))