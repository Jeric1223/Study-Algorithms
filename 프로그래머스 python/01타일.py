

d = [1] * 1000
n = int(input())
def tile01(n):
    for i in range(1,n+1):
        d[i] = d[i-1] + d[i-2] % 15746

tile01(n)
print(d[n])