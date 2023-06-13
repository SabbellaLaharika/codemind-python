n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in l :
    if i % 2 != 0 :
        cnt += 1
if cnt <= 2 :
    print("YES")
else :
    print("NO")