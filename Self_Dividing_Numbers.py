m = int(input())
n = int(input())
for i in range(m,n+1):
    t = i
    c = 0
    s = 0
    while i != 0 :
        d = i % 10
        i = i // 10
        c += 1
        if d == 0 :
            break
        if t % d == 0 :
            s += 1
    if s == c :
        print(t,end = " ")