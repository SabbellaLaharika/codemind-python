n = int(input())
l = list(map(int, input().split()))
k = int(input())
s = 0
for i in range(l.index(k)+1) :
    s += l[i]
print(s)