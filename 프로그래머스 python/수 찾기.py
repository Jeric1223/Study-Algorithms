#이진 탐색 구현하기
def BinarySearchBaek(input_list,searchValue):
    L = 0
    R = len(input_list)-1

    while(L <= R):
        M = (L+R)//2
        if input_list[M] < searchValue:
            L = M+1
        elif input_list[M] > searchValue:
            R = M-1
        elif input_list[M] == searchValue:
            print(1)
            break
    if L > R:
        print(0)

def Baekjun():
    n = int(input())
    A_list = list(map(int, input().split()))
    A_list.sort()
    n_t = int(input())
    B_list = list(map(int, input().split()))

    for i in B_list:
        BinarySearchBaek(A_list,i)
Baekjun()