n = int(input())
l = list(map(int, input().split()))
nl = list(set(l))
ml = []
if len(nl) >= 3 :
    nl.remove(max(nl))
    nl.remove(max(nl))
    print(max(nl))
else:
    print(max(nl))