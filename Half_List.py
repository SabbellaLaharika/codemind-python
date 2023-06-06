def half(l,n) :
    h = n//2
    nl = []
    for i in range(-1,-h-1,-1) :
        nl.append(l[i])
    for i in range(h) :
        nl.append(l[i])
    return nl
m = int(input())
ls = list(map(int, input().split()))
res = half(ls,m)
print(*res)