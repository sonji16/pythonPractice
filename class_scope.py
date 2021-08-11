def scope_test():
    spam = 'test spam'

def do_local():
    spam = 'local spam'

def do_nonlocal():
    nonlocal spam  # nonlocal 함수 밖의 spam을 사용하겠다고 선언
spam = 'nonlocal spam'

def do_global():
    global spam  # 무조건 전역변수 사용
spam = 'global spam'


# 1 로컬 스팸을 할당했지만 지역변수이므로 밖에서의 spam 값은 변화없음
do_local()
print('local 호출 뒤 :', spam)

# 2 가장 가까운 spam을 변화시켰으므로 현재 같은 레벨에서 spam 은 변화됨
do_nonlocal()
print('nonlocal 호출 뒤:', spam)

# 3 글로벌 spam에 할당했으므로 현재 같은 레벨에서 spam 값 변화없음
do_global()
print('global 호출 뒤:', spam)

scope_test()

# 현재 같은 레벨에 spam 이 없으므로 global spam 값을 출력함
print('함수 밖에서 호출:', spam)