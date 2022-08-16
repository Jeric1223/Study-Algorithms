n, m = map(int, input().split())
max_num = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_num = min(arr)
    max_num = max(max_num, min_num)
print(max_num)
