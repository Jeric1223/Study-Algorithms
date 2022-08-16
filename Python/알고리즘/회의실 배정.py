n = int(input())
input_arr = []
sum_n = 0
start = 0

for _ in range(n):
    input_arr.append(list(map(int, input().split())))
input_arr.sort(key=lambda x: (x[1], x[0]))

for i, item in enumerate(input_arr):
    if item[0] >= start or i == 0:
        sum_n += 1
        start = item[1]

print(sum_n)
