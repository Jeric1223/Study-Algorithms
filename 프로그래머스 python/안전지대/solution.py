def solution(board):
    n = len(board)
    answer_arr = [list(inner) for inner in board]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i-1 >= 0: # 위, 왼위, 오위
                    answer_arr[i-1][j] = 1 # 위 넣기
                    if j-1 >= 0:
                        answer_arr[i-1][j-1] = 1 # 왼위 넣기
                    if j+1 < n:
                        answer_arr[i-1][j+1] = 1 # 오위 넣기
                if i+1 < n: # 아래, 왼아, 오아
                    answer_arr[i+1][j] = 1 # 아래 넣기
                    if j-1 >= 0:
                        answer_arr[i+1][j-1] = 1 #왼아 넣기
                    if j+1 < n:
                        answer_arr[i+1][j+1] = 1 #오아 넣기
                if j-1 >= 0: # 왼
                    answer_arr[i][j-1] = 1 #왼 넣기
                if j+1 < n: # 오
                    answer_arr[i][j+1] = 1 #오 넣기

    total_sum = sum(sum(inner) for inner in answer_arr) 
    answer = (n*n) - total_sum # 전체 갯수 - 위험 지역
    
    return answer