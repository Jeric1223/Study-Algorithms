# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2024 KAKAO WINTER INTERNSHIP
# 가장 많이 받은 선물

def solution(friends, gifts):
    giftCountArr = [[0] * len(friends) for _ in range(len(friends))]
    giftDiffArr = [[0] * 3 for _ in range(len(friends))]

    # 선물 준 사람, 받은사람 카운팅 2차원 배열 세팅
    for item in gifts:
        give = item.split(' ')[0]
        receive = item.split(' ')[1]
        giftCountArr[friends.index(give)][friends.index(receive)] = giftCountArr[friends.index(give)][
                                                                        friends.index(receive)] + 1

    # giftDiffArr에 준 선물, 받은 선물, 선물 지수를 세팅한다.
    for index, value in enumerate(giftCountArr):
        giftDiffArr[index][0] = sum(value)
        giftDiffArr[index][1] = sum(giftCountArr[i][index] for i in range(len(giftCountArr)))
        giftDiffArr[index][2] = giftDiffArr[index][0] - giftDiffArr[index][1]

    # 정답 배열 세팅
    answer = [0 for _ in range(len(friends))]

    # 다음달에 받을 선물 갯수 카운팅
    for index, value in enumerate(giftCountArr):
        for child_index, child_value in enumerate(value):
            # 자신의 index랑 비교할 경우 나가기
            if child_index != index:
                # 상대가 준 선물갯수보다 내가 준 경우가 큰 경우
                if child_value > giftCountArr[child_index][index]:
                    answer[index] = answer[index] + 1
                # 만약 상대와 내가 준 갯수가 같을 경우
                elif child_value == giftCountArr[child_index][index]:
                    # 선물 지수가 클 경우 카운팅
                    if giftDiffArr[index][2] > giftDiffArr[child_index][2]:
                        answer[index] = answer[index] + 1
    return max(answer)
