n = int(input())
if 3 <= n <= 100 :
    for i in range(1,n+1) :
        for j in range(0,i):
            print("*",end = "")
        print()
    for i in range(1,n):
        for j in range(0,n-i):
            print("*",end = "")
        print()
else:
    print("The pattern is not possible")