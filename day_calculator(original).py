class Jiwoocalander:

    def test(self):
        while True:
            yyyymmdd = input('요일을 알고자 하는 년월일(AD양력)을 8자리로 입력해주세요(ex. 20200426)')

            # [양력] 00010101. 0001년. 1월. 1일. 월요일. 을 기준으로 함.
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

            # x는 0001년 1월 1일을 0일째로 하여 (year-1)년 12월 31일이 몇일째인지를 나타냄
            y_1 = int(year) - 1
            x = y_1 * 365 + (y_1 // 4) - (y_1 // 100) + (y_1 // 400)

            while True:
                result = x + int(date)  # result는 y = (year년 (month-1)월 마지막날이 1년1월1일 기준 몇일째인지를 나타내기 위해 중복되는 값을 변수로 묶은 것임
                if month == '1':
                    y = result
                elif month == '2':
                    y = result + 31
                elif month == '3':
                    y = result + 31 + 28
                elif month == '4':
                    y = result + 31 * 2 + 28
                elif month == '5':
                    y = result + 31 * 2 + 28 + 30
                elif month == '6':
                    y = result + 31 * 3 + 28 + 30
                elif month == '7':
                    y = result + 31 * 3 + 28 + 30 * 2
                elif month == '8':
                    y = result + 31 * 4 + 28 + 30 * 2
                elif month == '9':
                    y = result + 31 * 5 + 28 + 30 * 2
                elif month == '10':
                    y = result + 31 * 5 + 28 + 30 * 3
                elif month == '11':
                    y = result + 31 * 6 + 28 + 30 * 3
                elif month == '12':
                    y = result + 31 * 6 + 28 + 30 * 4
                else:
                    print('잘못된 날짜정보입니다')
                break

            if int(year) % 4 == 0:  # 윤년인 경우
                if int(month) > 2:
                    y = y + 1
            if int(year) % 100 == 0:
                y = y
            if int(year) % 400 == 0:
                if int(month) > 2:
                    y = y + 1



            idx = y % 7
            list_day = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
            print(list_day[idx])
        ###달력 만들기
















test = Jiwoocalander()
test.test()