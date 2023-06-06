def rotate(n,l,k) :
    nl = []
    mo = k % n
    for i in range(n-mo,n) :
        nl.append(l[i])
    for i in range(n-mo) :
        nl.append(l[i])
    return nl
t = int(input())
for i in range(t) :
    m,c = map(int, input().split())
    ls = list(map(int, input().split()))
    res = rotate(m,ls,c)
    print(*res)