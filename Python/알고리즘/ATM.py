n = int(input())
arr_input = list(map(int, input().split()))
sum_num = []
arr_input.sort()
for i, item in enumerate(arr_input):
    if i != 0:
        sum_num.append(sum_num[i-1] + item)
    else:
        sum_num.append(item)
print(sum(sum_num))
