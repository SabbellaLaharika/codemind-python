n,k,q = map(int, input().split())
l = list(map(int, input().split()))
ql = []
for i in range(q) :
    m = int(input())
    ql.append(m)
newl = []
r = k % n
for i in range(n-r,n) :
    newl.append(l[i])
for i in range(n-r) :
    newl.append(l[i])
for k in ql :
    for j in newl :
        if newl.index(j) == k :
            print(j)