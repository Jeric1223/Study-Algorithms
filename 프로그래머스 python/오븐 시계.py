h, m = map(int, input().split())
H = int(input())

if H >= 60:
    h += H//60
    m += H % 60

if h > 23:
    h -= 24

print(h,m)

