n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr.sort()
arr.sort(key=len)
print('\n'.join(arr))