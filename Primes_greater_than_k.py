def isprime(n) :
    cnt = 0
    for i in range(1,n) :
        if n % i == 0 :
            cnt += 1
    if cnt == 1 :
        return 1
    else :
        return 0
n = int(input())
l = list(map(int, input().split()))
k = int(input())
count = 0
for i in l :
    if isprime(i) :
        if i >= k :
            count += 1
print(count)