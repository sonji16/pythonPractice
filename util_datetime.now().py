import datetime
now = datetime.datetime.now()
print('현재시간:', now)

print('년:', now.year)
print('월:', now.month)
print('일:', now.day)
print('시:', now.hour)
print('분:', now.minute)
print('초:', now.second)

# 날짜 포맷 yyyyMMdd 출력하기 ex) 20200426
str_time = now.strftime('%Y%m%d')
print('%Y%m%d >>', str_time)

# 날짜 포맷 yyyyMMdd(요일) 출력하기 ex) 20200426(일)
str_time = now.strftime('%Y%m%d (%A)')
print('%Y%m%d (%A) >>', str_time)

# 날짜 포맷 yyyy-MM-dd hh:mm:ss로 출력하기 ex) 2020-04-26 17:51:45
str_time = now.strftime('%Y-%m-%d %H:%M:%S')
print('%Y-%m-%d %H:%M:%S >> ', str_time)