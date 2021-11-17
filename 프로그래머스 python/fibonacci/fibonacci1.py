d = [0] * 100
d[1] = 1
d[2] = 1

def fibonacci(n):
    if n == 2 or n == 1:
        return 1
    if d[n] != 0:
        return d[n]
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2)
    return d[n]

fibonacci(49)
print(d[:50])
#topDown

