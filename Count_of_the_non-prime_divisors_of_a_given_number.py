def prime(n) :
    cnt = 0
    for i in range(1,n) :
        if n % i == 0 :
            cnt += 1
    return cnt == 1
n = int(input())
count = 0
for i in range(1,n+1) :
    if n % i == 0 :
        if prime(i) == 0 :
            count += 1
print(count)