n = int(input())
cnt = 0
for i in range(1,n+1):
    if n // i == i + 1 :
        cnt = 1
        break
if cnt == 1 :
    print("YES")
else :
    print("NO")