list = [1, 2, 3, 4]

def Push(arr,params):
    arr.append(params)

def Pop(arr):
    if len(arr) == 0:
        print('리스트안에 값이 없어요')
    else:
        return arr[0:len(arr)-1]

Push(list, 1)
list = Pop(list)
print(list)