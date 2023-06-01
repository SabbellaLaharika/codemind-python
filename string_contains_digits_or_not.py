t = int(input())
for i in range(t) :
    s = input()
    cnt = 0
    for j in s :
        if j.isdigit() :
            cnt += 1
            break
    if cnt == 1 :
        print("Yes")
    else :
        print("No")