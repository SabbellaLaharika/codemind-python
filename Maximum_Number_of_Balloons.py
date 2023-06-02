s = input()
c = 0
b = s.count('b')
a = s.count('a')
l = s.count('l')
o = s.count('o')
n = s.count('n')
while (b != 0 and a != 0 and l != 1 and o != 1 and n != 0) :
    b -= 1
    a -= 1
    l -= 2
    o -= 2
    n -= 1
    c += 1
print(c)