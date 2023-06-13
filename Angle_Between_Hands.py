h,m = (input().split(':'))
ho = int(h)
mi = int(m)
anh = ho%12*30 + mi*0.5
anm = mi*6
angle = abs(anh-anm)
print(min(angle,360-angle))