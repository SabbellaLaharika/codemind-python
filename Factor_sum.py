def fac_sum(n):
    s = 0
    for i in range(1,n+1):
        if n % i == 0 :
            s += i
    return s
l = list(map(int, input().split(',')))
nl = []
for i in l :
    res = fac_sum(i)
    if res in l :
        nl.append(i)
if len(nl) == 0 :
    print(-1)
else :
    nl.sort()
    for i in nl :
        print(i,end = " ")