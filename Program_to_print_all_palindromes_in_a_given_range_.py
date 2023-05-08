a = int(input())
b = int(input())
for i in range(a,b+1) : 
    temp = i
    rev = 0
    while i != 0 :
        rem = i % 10
        i //= 10
        rev = rev*10 + rem
    if temp == rev :
        print(temp, end = " ")