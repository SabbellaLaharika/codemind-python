n = int(input())
l = list(map(int, input().split()))
cnt = 0
m = min(l)
for i in range(m,0,-1) :
    for j in l :
        if j % i != 0 :
            break
    else :
        print(i)
        break