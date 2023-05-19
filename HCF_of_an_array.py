n = int(input())
l = list(map(int, input().split()))
m = min(l)
z = 1
for _ in range(m,0,-1):
    c = 0
    for i in l:
        if i % _ != 0 :
            break
    else :
        print(_)
        break
    