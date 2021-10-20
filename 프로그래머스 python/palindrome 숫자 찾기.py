max = 0
max_i = 0
max_j = 0
tmp = 0
reverse_num = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        tmp = i*j
        reverse_num = int(str(tmp)[::-1])
        if tmp == reverse_num :
            if max < reverse_num:
                max = reverse_num
                max_i = i
                max_j = j
        else:
            continue;

print(f'{max_i} * {max_j} = {max}')