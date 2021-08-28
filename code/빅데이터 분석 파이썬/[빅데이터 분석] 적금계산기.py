salary, years = map(int,input("월급과 적금기간을 입력해 주세요: ").split())
name = input("이름을 넣어주세요 :")

#월급의 50%를 적금한다는 가정.

principal = int((salary//2)*(12*years)) #원금 계산
pre_tax_interest = int(principal*0.013) #세전이자 1.3%
interest_tax = int(pre_tax_interest*0.154) #이자과세 15.4%
sum = int(principal + (pre_tax_interest - interest_tax)) #세후 수령액

print(f"[대마뱅크]\n{name[0]}*{name[2]}님. 자유적금이 만기되어 알려드립니다")
print(f"원금: {principal:,}원")
print(f"세전이자: {pre_tax_interest:,}원")
print(f"이자과세(15.4%): {interest_tax:,}원")
print(f"세후 수령액: {sum:,}원")

# 2205 김재현