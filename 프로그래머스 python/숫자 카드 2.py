import sys


def LowerBound(find_arr, find_value):
    input_list = find_arr
    searchValue = find_value

    L = 0
    R = len(find_arr) - 1

    while(L < R):
        M = (L+R)//2
        if input_list[M] < searchValue:
            L = M+1
        else:
            R = M
    print(R + 1)

def UpperBound(find_arr, find_value):
    input_list = find_arr
    searchValue = find_value

    L = 0
    R = len(find_arr) - 1

    while(L < R):
        M = (L+R)//2

        if input_list[M] <= searchValue:
            L = M+1
        else:
            R = M
    print(R + 1)


n_input = int(sys.stdin.readline())
arr_input = list(map(sys.stdin.readline().split()))
find_input = int(sys.stdin.readline())
arr_find = list(map(sys.stdin.readline().split()))
answer = [0 for _ in range(n_input)]







