def solution(arr1, arr2):
    answer = []
    one_len = len(arr1)
    two_len = len(arr1[0])
    
    for i in range(one_len):
        arr_sum = []
        for j in range(two_len):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(arr_sum)
            
    return answer