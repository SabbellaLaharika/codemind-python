a,b = map(int, input().split())
if a == b-9 or b == a-9 or a == b-1 or b == a-1 :
    print("Yes")
else:
    print("No")