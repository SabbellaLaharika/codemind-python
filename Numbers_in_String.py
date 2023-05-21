s = input()
my_list = []
for i in s :
    if i.isdigit() :
        my_list.append(int(i))
print(sum(my_list))