n=int(input())
cnt = 0
i=2
while i<=(int(n**0.5)):
    if n%i == 0:
        cnt+=1
        break
    i+=1
if cnt==1:
    print("not a prime")
else:
    print("prime")