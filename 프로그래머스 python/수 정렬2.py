def main():
    n = int(input())
    input_list = []

    for _ in range(n):
        x, y = map(int, input().split())
        input_list.append([y, x])

    answer = sorted(input_list)

    for i in range(n):
        print(answer[i][1], answer[i][0])

main()