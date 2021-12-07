def solution(board, moves):
    answer = 0
    stack_arr = [0]

    for i in moves:
        for arr in board:
            if arr[i-1] != 0:
                if stack_arr[-1] == arr[i-1]:
                    stack_arr.pop()
                    arr[i-1] = 0
                    answer += 1
                else:
                    stack_arr.append(arr[i-1])
            else:
                continue

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))