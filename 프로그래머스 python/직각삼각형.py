done = True
list_input = []
answer_list = []

while(done):
    list_input = list(map(int,input().split()))
    if list_input[0] == 0 and list_input[1] == 0 and list_input[2] == 0:
        done = False
    else:
        list_input.sort()
        if list_input[2]**2 == list_input[0]**2 + list_input[1]**2:
            answer_list.append("right")
        else:
            answer_list.append("wrong")

print('\n'.join(answer_list))