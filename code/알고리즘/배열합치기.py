A_n, B_n = map(int, input().split())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))
answer_arr = []

i = 0
j = 0

while i < A_n and j < B_n:
    if A_arr[i] > B_arr[j]:
        answer_arr.append(B_arr[j])
        j += 1
    else:
        answer_arr.append(A_arr[i])
        i += 1

print(*(answer_arr + (A_arr[i:] if i < A_n else B_arr[j:])))
