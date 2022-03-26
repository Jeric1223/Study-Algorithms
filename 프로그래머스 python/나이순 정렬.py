def swap(arr,x,y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp

n = int(input())
arr = []

for _ in range(n):
    age,name = input().split()
    arr.append([age,name])

arr = sorted(arr,key= lambda x: (x[0]))

for x,y in arr:
    print(x,y)
