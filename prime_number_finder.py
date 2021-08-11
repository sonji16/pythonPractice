import time
# 숫자 입력 받기
while True:
    try:
        original_number = int(input('소수를 찾고자 하는 최대의 수를 입력해주세요: '))
        if original_number <= 1:  # 입력한 정수가 1 이하일 때
            print('2 이상의 정수를 입력해주세요')
        else:  # 입력한 수가 조건을 만족할 때
            break
    except ValueError:  # 입력한 수가 정수가 아닐 때
        print('2 이상의 정수를 입력해주세요')

# 변수 선언
prime_number = [2]  # 입력한 2 이상 정수 이하의 소수를 이 리스트에 저장
calculate_num = 0

# 소인수를 리스트에 저장하기/ 숫자 판정
start = time.time()  # 연산 시간 재기

for my_number in range(3, original_number + 1):  # 3부터 입력한 수까지 -> 판정하려는 수
    divide_number = 2
    prime_number.append(my_number)
    while divide_number < my_number:
        if my_number % divide_number == 0:
            prime_number.remove(my_number)
            break
        divide_number += 1
        #calculate_num += 1

print('코드 실행시간: ', time.time() - start, '초')
print('소수: ', prime_number)
print('소수의 개수: ', len(prime_number))
print('연산횟수:', calculate_num)


