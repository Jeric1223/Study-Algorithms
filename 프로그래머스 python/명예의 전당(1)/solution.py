def solution(k, score):
    answer = [0] * k
    result = []
    scoreCount = 0
    for item in score:
        scoreCount += 1
        answer.sort(reverse=True)
        for i, answerItem in enumerate(answer):
            if item >= answerItem:
                answer.insert(i, item)
                answer.pop()
                break
        if scoreCount >= k:
            result.append(answer[-1])
        else:
            result.append(answer[scoreCount-1])
    return result