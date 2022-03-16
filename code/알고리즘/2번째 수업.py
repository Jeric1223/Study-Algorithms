

def bubbleSort(arr):
    n = len(arr)
    arr1 = arr

    for i in range(n):
        for j in range(n-1):
            if arr1[j] > arr1[j+1]:
                tmp = arr1[j]
                arr1[j] = arr1[j+1]
                arr1[j+1] = tmp

    print(' '.join(map(str,arr)))

def bubbleType2(arr, strArr):
    n = len(arr)
    arr1 = arr
    answer = [0,0,0]

    Aindex = strArr.index('A')
    Bindex = strArr.index('B')
    Cindex = strArr.index('C')

    for i in range(n):
        for j in range(n-1):
            if arr1[j] > arr1[j+1]:
                tmp = arr1[j]
                arr1[j] = arr1[j + 1]
                arr1[j + 1] = tmp

    answer[Aindex] = arr1[0]
    answer[Bindex] = arr1[1]
    answer[Cindex] = arr1[2]

    print(' '.join(map(str,answer)))


def BaeJun():
    arr = list(map(int,input().split()))
    str = input()
    strArr = list(str)
    bubbleType2(arr,strArr)

def GongChange():
    N, M = map(int,input().split(' '))
    changeNumDic = []

    for i in range(M):
        a, b = map(int,input().split(' '))
        changeNumDic.append({'i':a,'j':b})
    arr = [i for i in range(1,N+1)]

    for value in changeNumDic:
        i = value['i']
        j = value['j']
        arr[i-1],arr[j-1] = arr[j-1],arr[i-1]
    print(' '.join(map(str,arr)))

def BaejunType2():
    n = int(input())
    arr = []

    for _ in range(n):
        n = input()
        arr.append(n)
    arr.sort()
    print('\n'.join(map(str, arr)))

def BaekJun2839():
    n = int(input())
    testNum = n%5
    if testNum%3 != 0:
