my_pw = '{NYPc2019}'  # input('비밀번호를 입력해주세요.')
my_pw_list = list(my_pw)
print('입력한 비밀번호: ', my_pw)

special_character = '`!@#$%^&*()-=_+|;:\'\"/?,.<>~[]{}``'
lower_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
upper_alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
special_character_list = list(special_character)
lower_alphabet_list = list(lower_alphabet)
upper_alphabet_list = list(upper_alphabet)

have_lower_alphabet = 0
have_upper_alphabet = 0
have_special_character = 0
not_allowed = True
length_st = True
result = []

if len(my_pw) > 15 or len(my_pw) < 8:
    length_st = False


for this_pw in my_pw_list:
    if this_pw in lower_alphabet_list:
        have_lower_alphabet += 1
    elif this_pw in upper_alphabet_list:
        have_upper_alphabet += 1
    elif this_pw in special_character_list:
        have_special_character += 1

if have_upper_alphabet + have_lower_alphabet + have_special_character < len(my_pw_list):
    not_allowed = False
print(have_special_character, have_lower_alphabet, have_upper_alphabet, not_allowed)
if have_lower_alphabet == 0:
    result.append('소문자')
elif have_upper_alphabet == 0:
    result.append('대문자')
elif have_special_character == 0:
    result.append('특수문자')

# 문제에서 제시한 출력 형태
if len(result) == 0 and not_allowed == False and length_st == True:
    print('valid')
else:
    print('invalid')

    
# 내가 만든 출력 형태
"""
if len(result) == 0 and not_allowed == False and length_st == True:
    print('사용할 수 있는 비밀번호 입니다')
elif length_st == False:
    print('8자 이상 15자 이하로 입력해주세요')
else:
    print(result, '가 반드시 포함되어야 합니다.')

if not_allowed == True:
    print('특수문자는 !@#$%^&*()-=_+|;:\'\"/?,.<>~[]{}` 만 입력할 수 있습니다')
"""