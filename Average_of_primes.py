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
new = []
for i in l :
    if isprime(i) :
        new.append(i)
avg = sum(new)/len(new)
print(f'{avg :.2f}')