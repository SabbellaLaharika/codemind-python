def rev(n) :
    rev = 0
    while n != 0 :
        rem = n % 10
        rev = rev*10 + rem
        n //= 10
    return rev
def pal(n) :
    t = n 
    if t == rev(n) :
        return 1
    return 0
x = int(input())
while 1 :
    x = x + rev(x)
    if(pal(x)) :
        print(x)
        break