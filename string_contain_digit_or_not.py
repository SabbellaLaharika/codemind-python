s = input()
cnt = 0
for i in s :
    if i.isdigit() :
        cnt += 1
if cnt :
    print(f'Contains {cnt} digit')
else :
    print("Doesn't contain digit")