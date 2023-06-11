n = int(input())
l = list(map(int, input().split()))
p = 1
for i in l :
    p *= i
nl = []
for i in l :
    nl.append(p//i)
print(*nl)