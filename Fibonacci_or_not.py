n = int(input())
cnt = 0
a = 0
b = 1
for i in range(1,n+1): 
    f = a + b
    if f == n :
        cnt += 1
        break
    a = b
    b = f
print(cnt != 0)