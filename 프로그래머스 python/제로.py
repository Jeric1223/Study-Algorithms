n = int(input())
arr = []
for i in range(n):
    n_n = int(input())
    if n_n == 0:
        arr.pop(arr.index(arr[-1]))
    else:
        arr.append(n_n)
print(sum(arr))