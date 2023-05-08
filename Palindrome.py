n = int(input())
i = 0
rev = 0
temp = n
while n != 0 :
    rem = n % 10
    n //= 10
    rev = rev*10 + rem
print(temp == rev)