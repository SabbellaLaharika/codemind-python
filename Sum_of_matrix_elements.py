m = int(input())
n = int(input())
mat = []
for i in range(m) :
    l = list(map(int, input().split()))
    mat.append(sum(l))
print(sum(mat))