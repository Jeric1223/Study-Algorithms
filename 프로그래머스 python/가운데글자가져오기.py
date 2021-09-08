a = input()
tmp =0
temp = 0

if len(a)%2 == 0:
    tmp = int(len(a)/2)
    print(a[tmp-1:tmp+1])
elif len(a)%2 == 1:
    temp = round(len(a)/2)
    print(a[temp])