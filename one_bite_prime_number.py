# 55 튜플 = 값 변경 불가
# clovers_1 = (1, 2, 3)
# clovers_2  = [1, 2, 3]
# clovers_2[2] = 4
# print (clovers_2[2])

# 56 패킹, 언패킹
# clovers = 1, 2, 3
# print(clovers)
# r, g, b = 240, 248, 255
# print(r, g, b)

# 57 패킹, 언패킹 예제(사탕 바꾸기)
# dodo = '박하맛'
# alice = '딸기맛'
# dodo, alice = alice, dodo
# print('도도새:', dodo,'앨리스:', alice)

# 58 Dictionary 기본구조
# # 파이썬 = 비단뱀
# my_dict1 = {}
# print(my_dict1)
# my_dict2 = {'이름': '앨리스', '나이': 10, '시력': [1,0, 1.2]}
# print(my_dict2)

# 59 딕셔너리 값 바꾸기
# dic = {}
# dic[0] = 1
# dic[1] = 2
# print(dic)
# dic[0] = 3
# print(dic)

# 61 딕셔너리 값 print 하기(.get)
# jiwoo = {'age': 17, 'job': 'student','number': 10119}
# print(jiwoo['number'])
# print(jiwoo['age'])
# print(jiwoo.get('job'))

# 62 딕셔너리 키, 값 제거
# jiwoo = {'age': 17, 'job': 'student', 'number': 10119}
# del jiwoo['age']
# print(jiwoo)

# 63 딕셔너리 예제(라면 주문)
# order = {'spade1': 'bibim_ramen', 'dia2': 'spicy_ramen'}
# print(order)
# order['clover3'] = 'curry_ramen'
# print(order)
# order['dia2'] = '짜장라면'
# print(order)
# del order['spade1']
# print(order)

# 64 함수 종류
# 내장함수 built in function
# 모듈의 함수
# 사용자 정의 함수

# 65 함수의 기본 구조
# def 함수이름(인수):
    # 실행할 명령
    #return 반환값

# def my_func():
    # print('토끼야 안녕')

# def add(num1, num2):
    # return num1 + num2

# print(add(2,3))

# def add_mul(num1, num2):
    # return num1 + num2, num1*num2
# print(add_mul(5,6))

# 66 함수 이용해서 반복 피하기
# def judge_cards(name):
    # print(name, '1 유죄!')
    # print(name, '2 유죄!')
    # print(name, '3 유죄!')
# judge_cards('하트')
# judge_cards('클로버')
# judge_cards('스페이드')

# 67 모듈
# 모듈: 다른 사람들이 만들어놓은 것들
# import 모듈이름.함수이름

# 68 모듈- 랜덤하게 뽑기(random. choice/sample/randint)
# import random
# animals = [1, 2, 3, 4, 5, 6, 7]
# print(random.choice(animals)) # 랜덤 한개 뽑기
# print(random.sample(animals, 2)) # 랜덤 중복없이 두개 뽑기
# print(random.randint(5, 10)) # 5~10정수 중 하나를 랜덤 뽑기

# 69 랜덤으로 뽑기 예제(죄인뽑기)
# import random
# cards = ['하트', '클로버', '스페이드']
# chosen_card = random.choice(cards)
# print(chosen_card, '유죄!')

# 70 모듈을 사용하는 이유
# 이미 만들어진 것을 이용하여 간결하고 쉽게 만들기 위해서

# 71~ 연습문제
# print(3 + 1 - 2)
# print(3 - 1 + 2)
# print(3/1 - 2)
# 4
# 1
# 2
# 24

# adcdef
# 1


# 73 연습문제(3)
# nums = [1, 2, 3]
# print(nums)
# []

# fruits = ['자몽', '멜론', '레몬']
# print(fruits)
# del fruits[0]
# print(fruits)

# 74 연습문제(2)
# nums = [1, 3]
# nums[1] = 2
# nums.append(3)
# nums.append(4)
# print(nums)

# 3
# 3

# 1, 2, 3,
# 3, 4, 5

# 75 횟수로 반복하기 연습문제(1)
# fruits = ['멜론', '거봉', '레몬']
# print(fruits)
# fruits.sort()
# print(fruits)
# for num in [3, 1, 2]:
   # print(num)
# for num in range(2):
    # print(num)
# clovers = ['클로버1', '클로버2', '클로버3']
# for clover in clovers:
   #  print(clover)

# clovers = ['클로버1', '클로버2', '클로버3']
# for idx in range(3):
   #  print(clovers[idx]

# for i in range(1,4):
    # print('*'*i)
# stars = [2, 1, 3]
# for num in stars:
    # print('*'*num)

# total = total + num

# total = 0
# card_nums = [1, 3, 6, 7]
# for num in card_nums:
    # total = total + num
# print(total / len(card_nums))

# switch = 'on'
# if switch == 'on':
    # print('조명이 켜졌어요.')
# else:
    # print('조명이 꺼졌어요.')

# input_number = -9
# if input_number >= 0:
    # absolute_value = input_number
# else:
    # absolute_value = -(input_number)
# print(absolute_value)

# 총 주문금액은 18500원입니다.

# odd_nums = []
# for num in range(10):
    # if num % 2 != 0:
        # odd_nums.append(num)
# print(odd_nums)

# 윤년 계산하기
# year = 2016
# if year % 400 == 0:
    # print(year, '년은 윤년입니다.')
# elif year % 4 == 0 and year % 100 != 0:
    # print(year, '년은 윤년입니다.')
# else:
    # print(year, '년은 윤년이 아닙니다.')

# 1~5까지 총합 구하기
# count = 1
# while count < 4:
    # count = count + 1
    # print(count)

# total = 0
# count = 1
# while count <= 5:
    # total = total + count
    # count = count + 1
# print('총합은', total)

# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))

#3부터 1까지 거꾸로 세기
# count = 3
# while count >= 1:
    # print(count)
    # count = count - 1

# num = 1
# while True:
    # print(num)
    # num = num + 1

    # if num > 3:
        # break

# price = 0
# while price != -1:
    # price = int(input('가격을 입력하세요 (종료:-1):'))
    # if price> 10000:
        # print('너무 비싸요')
    # elif price > 5000:
        # print('괜찮은 가격이네요.')
    # elif price > 0:
        # print('정말 싸요.')


# 소수 판정하기
while True:
    number = int(input('2 이상의 정수를 입력하세요(종료: -1):'))
    if number == -1:
        break
    count = 2
    is_prime = True
    while count < number:
        if number % count == 0:
            is_prime = False
            break
        count = count + 1

    if number >= 2:

        if is_prime:
            print(number, '은(는) 소수입니다.')
        else:
            print(number, '은(는) 소수가 아닙니다.')

    else:
        '2 이상의 정수를 입력하세요.'


