def main():
    n = int(input())
    input_list = []

    for _ in range(n):
        x, y = map(int, input().split())
        input_list.append([x, y])

    answer = sorted(input_list)

    for i in range(n):
        print(answer[i][0], answer[i][1])

main()