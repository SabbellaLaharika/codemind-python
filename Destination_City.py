n = int(input())
l = []
for i in range(n) :
    ls = list(map(str, input().split()))
    l.append(ls)
for i in range(n) :
    cnt = 0
    for j in range(n) :
        if l[i][1] == l[j][0] :
            cnt += 1
    if cnt == 0 :
        print(l[i][1]) 
        break