n = int(input())
P_arr = list(map(int,input().split()))
m = n+1
D_arr = [0]*m
MAX_arr = []

for i in range(0,n+1):
    for j in range(0,i):
        MAX_arr.append(P_arr[j]+D_arr[i-j-1])
    if len(MAX_arr) != 0:
        D_arr[i] = max(MAX_arr)
    MAX_arr = []

print(D_arr[-1])
