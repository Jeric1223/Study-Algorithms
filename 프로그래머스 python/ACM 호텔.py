n = int(input())
list_input = []
answer_list = []

for _ in range(n):
    H,W,N = map(int,input().split())
    if H == 1 and W == 1 and N == 1:
        answer_list.append('101')
    else:
        if N//H + 1 < 10:
            ho = f'{0}{N//H + 1}'
        else:
            ho = N//H + 1
        height = N//H if N%H == 0 else N%H
        answer_list.append(f'{height}{ho}')

print('\n'.join(answer_list))