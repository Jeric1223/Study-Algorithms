n = int(input())
money = [500,100,50,10,5,1]
input_money = 1000 - n
sum_num = 0

for item in money:
    if input_money == 0:
        break
    else:
        if input_money // item != 0:
            sum_num += input_money//item
            input_money = input_money % item

print(sum_num)