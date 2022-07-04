n, h, k = map(int, input().split())
tower = list(map(int, input().split()))[:n]

result = 0
for i in range(n):
    if i-k >= 0 and i+k < n:
        if max(tower[i-k:i+k]) < h:
            result += 1
print(result)
