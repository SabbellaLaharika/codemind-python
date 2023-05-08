n = int(input())
a = 0
b = 1
for i in range(0,n):
    print(a,end = " ")
    f = a + b
    a = b
    b = f