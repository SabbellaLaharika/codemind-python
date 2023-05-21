n = str(input())
s = 0
for i in range(len(n)):
    s += int(n[i])**(i+1)
print(int(n) == s)
