n = int(input())
l = list(map(int, input().split()))
f = int(input())
fl = []
for i in range(n) :
    if l[i] == f :
        fl.append(i)
if len(fl) != 0 :
    res = [min(fl),max(fl)]
    print(*res)
else :
    print(*[-1,-1])