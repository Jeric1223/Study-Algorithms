#이진 탐색 구현하기
def BinarySearch():
    n = int(input('데이터의 값을 입력해 주세요. : '))
    input_list = list(map(int,input().split()))
    searchValue = int(input())

    L = 0
    R = n-1

    while(L <= R):
        M = (L+R)//2
        if input_list[M] < searchValue:
            L = M+1
        elif input_list[M] > searchValue:
            R = M-1
        elif input_list[M] == searchValue:
            print(f'{M}번째 인덱스에 있습니다.')
            break
    else:
        print('데이터 값이 없어요')

#lower bound 구현하기
def LowerBound():
    n = int(input('데이터의 값을 입력해 주세요. : '))
    input_list = list(map(int,input().split()))
    searchValue = int(input())

    L = 0
    R = n-1
    M_INDEX = 0

    while(L < R):
        M = (L+R)//2
        if input_list[M] < searchValue:
            L = M+1
        else:
            R = M
        M_INDEX = M
    print(R + 1)

#UpperBound bound 구현하기
def UpperBound():
    n = int(input('데이터의 값을 입력해 주세요. : '))
    input_list = list(map(int,input().split()))
    searchValue = int(input())

    L = 0
    R = n-1

    while(L < R):
        M = (L+R)//2

        if input_list[M] <= searchValue:
            L = M+1
        else:
            R = M
    print(R + 1)
UpperBound()
