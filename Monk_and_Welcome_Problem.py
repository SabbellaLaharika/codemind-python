n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n) :
    c.append(a[i]+b[i])
for i in range(n) :
    print(c[i], end = " ")