def per_sq(n) :
    f = n**(0.5)
    i = int(n**0.5)
    return f == i
n = int(input())
l = map(int, input().split())
s = 0
for i in l :
    if per_sq(i) :
        s += i
print(s)