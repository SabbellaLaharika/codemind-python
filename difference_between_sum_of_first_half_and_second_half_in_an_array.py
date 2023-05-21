n = int(input())
l = list(map(int, input().split()))
s = sum(l)
en = 0
on = 0
if n % 2 == 0 :
    for i in range(n//2) :
        en += l[i]
    sp = s - en
    print(abs(sp-en))
else :
    for i in range((n-1)//2) :
        on += l[i]
    sp = s - on
    print(abs(sp-on))