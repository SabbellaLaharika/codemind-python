n = int(input())
l = 2*n - 1
for i in range(l):
    for j in range(l):
        if i < j :
            val = i
        else:
            val = j
        if val >= l - i :
            val = l - i - 1
        if val >= l - j :
            val = l - j - 1
        print(n-val,end = " ")
    print()