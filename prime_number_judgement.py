check = False  # 숫자 입력 받기
while not check:
    try:
        my_number = int(input('소인수분해를 하고자 하는 2 이상의 정수를 입력하세요: '))
        if my_number <= 1:  # 입력한 정수가 1 이하일 때
            print('2 이상의 정수를 입력해주세요')
        else:  # 입력한 수가 조건을 만족할 때
            check = True
    except ValueError:  # 입력한 수가 정수가 아닐 때
        print('2 이상의 정수를 입력해주세요')


# 변수 선언
divide_number = 2
prime_factor = []  # 입력한 2 이상 정수의 소인수를 이 리스트에 저장
divide_number_turn = 1
revised_number = my_number
# 소인수를 리스트에 저장하기/ 숫자 판정
# check = False
# stop = False
# while not stop:
    # for num in range(2, my_number):
       # while not check:
            # if revised_number % num == 0:
                # prime_factor.append(num)
                #revised_number = (revised_number / num)
                #if revised_number == 1:
                    #check = True
                    #stop = True
            #elif revised_number % num != 0:
                #check = True

while divide_number < my_number:
    if my_number % divide_number == 0:
        prime_factor.append(divide_number)
        divide_number += 1
    else:
        divide_number += 1

# 리스트에 존재하는 숫자의 유무를 바탕으로 소수와 합성수 구분하기
if len(prime_factor) == 0:
    print('소수입니다')
else:
    print('합성수입니다')
    # print('소인수는 ', prime_factor)

