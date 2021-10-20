def solution(answers):
    # 수포자 1 번 12345
    # 수포자 2 번 21232425
    # 수포자 3 번 3311224455
    frist_person = [1, 2, 3, 4, 5]
    second_person = [2, 1, 2, 3, 2, 4, 2, 5]
    third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score_arr = [0, 0, 0]
    max = 0
    answer = []

    for index, item in enumerate(answers):
        if item == frist_person[index % 5]:
            score_arr[0] += 1
        if item == second_person[index % 8]:
            score_arr[1] += 1
        if item == third_person[index % 10]:
            score_arr[2] += 1

    for item in score_arr:
        if (max < item):
            max = item

    for i, item in enumerate(score_arr):
        if (max == item):
            answer.append(i + 1)

    return answer   