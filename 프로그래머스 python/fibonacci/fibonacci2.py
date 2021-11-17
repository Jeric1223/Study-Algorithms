d = [0] * 101
d[1] = 1
n = 5

def fibonacci(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        else:
            d[i] = d[i-1] + d[i-2]

fibonacci(n)
print(d[n])
#bottomUp