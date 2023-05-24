# 백준 국회의원 선거

# 입력을 리스트와 찾고싶은 value를 넣어서 해당 값이 같은 값의 인덱스 위치를 배열로 보내준다.
def find_all_indices(lst, value):
    indices = []
    for i, x in enumerate(lst):
        if x == value:
            indices.append(i)
    return indices

def __main__():
    n =  int(input())
    vote_list = []

    # 해당 기호의 투표수 가져오는 코드
    for i in range(n):
        item = int(input())
        vote_list.append(item)

    result = 0
    while True:
        MAX = max(vote_list)
        indices = find_all_indices(vote_list, MAX)

        # 기호 1번이 독보적인 최다 투표자가 되면 break
        if len(indices) == 1 and indices[0] == 0:
            break
        else:
            # 제일 큰 인덱스를 가지고 있는 것들에서 뒤에서부터
            index = indices[-1]
            # 가장 큰 값을 -1 시키기
            vote_list[index] = vote_list[index] - 1
            # 기호 1번을 +1 시키기
            vote_list[0] = vote_list[0] + 1
            # 정답 더하기
            result += 1

    print(result)

__main__()


