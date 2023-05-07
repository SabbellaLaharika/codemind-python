t = int(input())
for i in range(t):
    n,a,b,k = map(int, input().split())
    appy = 0
    chef = 0
    nac = 0
    appy = n//a
    chef = n//b
    nac = n//(a*b)
    total = appy + chef - nac
    if(total>=k):
        print("Win")
    else:
        print("Lose")