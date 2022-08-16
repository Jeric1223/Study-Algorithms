N,K = map(int, input().split())
input_arr = []
sum_num = 0

for _ in range(N):
    input_arr.append(int(input()))

input_arr.sort(reverse=True)

for item in input_arr:
    if K == 0:
        break
    else:
        if K // item != 0:
            sum_num += K // item
            K = K % item
print(sum_num)