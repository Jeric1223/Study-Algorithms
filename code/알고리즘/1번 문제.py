def maxFunc():
    arr = list(map(int, input().split()))
    tmp = max(arr)
    index = arr.index(tmp)
    print(tmp)
    print(index +1)

def minMaxFunc():
    n = input()
    arr = list(map(int,input().split()))
    arr.sort()
    print(arr[0],arr[-1])

def SAM69():
    n = int(input())
    for i in range(1,n+1):
        if i%3==0:
            print('X', end=' ')
        else:
            print(i, end=' ')

def SAM69Type2():
    n = int(input())
    num = 0
    for i in range(1,n+1):
        while(i):
            if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
                num += 1
            i = i//10
    print(num)


