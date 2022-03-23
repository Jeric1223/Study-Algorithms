n = int(input())
input_list = list(map(int, input().split()))
s = int(input())

count = 0

while s > 0:
    if input_list[count:s+count] == []:
        break
    else :
        x = input_list[count:s+count+1 ]
        max_index = input_list.index(max(x))
        if count != max_index:
            s = s - (max_index - count)
            input_list.insert(count, input_list[max_index])
            input_list.pop(max_index+1)

        count += 1

print(*input_list)
