n = int(input())
rem = 0
sq = n**2
s = 0
while sq != 0 :
    rem = sq % 10
    s += rem
    sq //= 10
if s == n :
    print("Neon Number")
else:
    print("Not Neon Number")