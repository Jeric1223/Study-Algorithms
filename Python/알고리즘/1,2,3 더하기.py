test_case = int(input())
input_arr = []

for i in range(test_case):
    input_arr.append(int(input()))

def answer(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return answer(n-1) + answer(n-2) + answer(n-3)

for input_item in input_arr:
    print(answer(input_item))