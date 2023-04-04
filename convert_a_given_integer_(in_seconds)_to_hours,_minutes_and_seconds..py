sec=int(input())
h=sec//3600
m=(sec-3600*h)//60
s=sec-60*m-3600*h
print(f'H:M:S-{h}:{m}:{s}')