N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

a_answer = 0
b_answer = 0

for i in range(N):
    if A_arr[i] == B_arr[i]:
        a_answer += 1
    else:
        for j in range(N):
            if A_arr[i] == B_arr[j]:
                b_answer += 1

print(a_answer)
print(b_answer)