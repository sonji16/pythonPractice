# 컴퓨터와 가위바위보 게임

#random 라이브러리 임포트
from random import *
ran = Random()
print('\n\n가위 바위 보 게임 시작')
list_dice= ['가위', '바위','보']
man = input('가위 or 바위 or 보 중 하나를 입력하세요 " =>')
ai = list_dice[ran.randrange(0, 3)]

print('사람은 %s'% man)
print('컴퓨터는 %s'% ai)
if man == '가위' and ai == '보':
    print('사람 승')
elif man == '바위' and ai == '가위':
    print('사람 승')
elif man == '보' and ai == '바위':
    print('사람 승')
elif man == '가위' and ai == '바위':
    print('컴퓨터 승')
elif man == '바위' and ai == '보':
    print('컴퓨터 승')
elif man == '보' and ai == '가위':
    print('컴퓨터 승')
else:
    print('비김')