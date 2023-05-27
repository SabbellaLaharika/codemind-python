def isprime(z):
    cnt = 0
    for _ in range(1,z) :
        if z % _ == 0 :
            cnt += 1
    if cnt == 1 :
        return 1
    else :
        return 0
n = int(input())
arr = list(map(int, input().split()))
np = 1
p = 1
for i in arr :
    if isprime(i) == 1 :
        p *= i
    else :
        np *= i
print(abs(np-p))