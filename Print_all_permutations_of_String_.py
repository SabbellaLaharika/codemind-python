from itertools import permutations
s = input()
l = list(permutations(s,len(s)))
for i in l :
    print("".join(i))