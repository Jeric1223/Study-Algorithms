A, B, C = map(int, input().split())
def calc(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a % C
    elif b % 2 == 0:
        temp = calc(a, b//2)
        return (temp * temp) % C
    else:
        return a * calc(a, b - 1) % C

print(calc(A,B))
