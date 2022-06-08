from collections import Counter

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

count = Counter(n_arr)

print(count)

for i in range(len(m_arr)):
    if m_arr[i] in count:
        print(count[m_arr[i]], end=' ')
    else:
        print(0, end=' ')



