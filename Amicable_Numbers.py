def fac_sum(n) :
    s = 0
    for i in range(1,n):
        if n % i == 0 :
            s += i
    return s
a = int(input())
b = int(input())
if a == fac_sum(b) and b == fac_sum(a) :
    print("Amicable")
else:
    print("Not Amicable")