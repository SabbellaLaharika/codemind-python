n = int(input())
x = n
if n < 0 :
    n = n * -1
rev = 0
if n > 0 :
    while(n!=0) :
        rem = n % 10
        rev = rev*10 + rem 
        n //= 10
if x < 0 :
    rev = rev* -1
print(rev)