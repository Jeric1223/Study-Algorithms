import datetime as dt
import calendar

"""
 datetime 함수안에 월 일 넣기
 datetime 시간대가 UST기준으로 나와서 고쳐야함
"""
a, b = map(int, input().split())


t = dt.datetime(2016,a,b,0,0,0)
sum_time = t + dt.timedelta(hours=9)
weekday = calendar.day_name[sum_time.weekday()]

str = weekday.upper()
print(f"{str[0:3]}")