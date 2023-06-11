t = int(input())
for i in range(t) :
    m,n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    nl = []
    for i in a :
        nl.append(i)
    for i in b :
        nl.append(i)
    nl.sort()
    print(*nl)