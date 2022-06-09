N, M, V = map(int, input().split())
all_arr = []
A = [[0 for col in range(0)] for row in range(M+1)]
check = [0 for row in range(M+1)]
stack = []
queue = []

for i in range(M):
    x, y = map(int, input().split())
    all_arr.append([x, y])

for item in range(M):
    #인접 리스트 만들기
    if item <= M-1:
        A[all_arr[item][0]].append(all_arr[item][1])
        A[all_arr[item][1]].append(all_arr[item][0])
    
print(check)
print(A)
