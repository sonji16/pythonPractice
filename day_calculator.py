
while True:
    yyyymmdd = input('요일을 알고자 하는 년월일(AD양력)을 8자리로 입력해주세요(ex. 20200426)')

    # [양력] 00010101. 0001년. 1월. 1일. 금요일. 을 기준으로 함.
    year = yyyymmdd[:4]
    month = yyyymmdd[4:6]
    date = yyyymmdd[-2:]

    if year[0] == '0':
        year = year[1:]
        if year[0] == '0':
            year = year[1:]
            if year[0] == '0':
                year = year[1:]
                if year == '0':
                    print('잘못된 날짜정보입니다')
                    continue
    if month[0] == '0':
        month = month[1:]
        if month[0] == '0':
            print('잘못된 날짜정보입니다')
            continue

    if date[0] == '0':
        date = date[1:]
        if date[0] == '0':
            print('잘못된 날짜정보입니다')
            continue

    # leap_year_num_since00010101 = year/4
    # x는 0001년 1월 1일을 1일째로 하여 (year-1)년 12월 31일이 몇일째인지를 나타냄
    x = (int(year) -1) * 365 + ((int(year)//4)-1)



    result = x + int(date) # result는 y = (year년 month월 1일이 몇일째인지)를 나타내기 위해 중복되는 값을 변수로 묶은 것임
    if month == '1':
        y = result
    elif month == '2':
        y = result + 31
    elif month == '3':
        y = result + 31 + 28
    elif month == '4':
        y = result + 31*2 + 28
    elif month == '5':
        y = result + 31*2 + 28 + 30
    elif month == '6':
        y = result + 31*3 + 28 + 30
    elif month == '7':
        y = result + 31*3 + 28 + 30*2
    elif month == '8':
        y = result + 31*4 + 28 + 30*2
    elif month == '9':
        y = result + 31*5 + 28 + 30*2
    elif month == '10':
        y = result + 31*5 + 28 + 30*3
    elif month == '11':
        y = result + 31*6 + 28 + 30*3
    elif month == '12':
        y = result + 31*6 + 28 + 30*4
    else:
        print('잘못된 날짜정보입니다')

    if int(year) % 4 == 0: # 윤년인 경우
        if int(month) > 2:
            y = y + 1


    # z는 최종 날짜수로, 0001년 1월 1일을 0일째, 0001년 1월 2일을 1일째로 했을 때,  year년 month월 date일이 몇일째인지를 나타내는 변수
    z = y - 1

    if z % 7 == 0:
        print('일요일')
    elif z % 7 == 1:
        print('월요일')
    elif z % 7 == 2:
        print('화요일')
    elif z % 7 == 3:
        print('수요일')
    elif z % 7 == 4:
        print('목요일')
    elif z % 7 == 5:
        print('금요일')
    elif z % 7 == 6:
        print('토요일')