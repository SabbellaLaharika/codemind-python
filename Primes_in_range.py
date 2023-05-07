def isprime(n):
    if n == 2:
        return 0
    else:
        i = 2
        while i <= n**0.5 :
            if n % i == 0:
                return 0
            i += 1
        else:
            return 1
a = int(input())
b = int(input())
count = 0
for j in range(a,b+1):
    count += isprime(j)
print(count)