n = int(input())
l = list(map(int, input().split()))
m = max(l)
z = 1
while (1) :
    c = 0
    for i in l:
        if (m*z) % i == 0 :
            c += 1
    if c == n :
        break
    z += 1
print(m*z)