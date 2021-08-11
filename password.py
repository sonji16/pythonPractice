# url의 값을 바꾸면서 사이트별 다른 비밀번호를 생성할 수 있음

url = "http://daum.net"
name = url[7:-4]
password = name[:3] + str(len(name)) + str(name.count("e")) + "!"

print(password)
print("{0}의 비밀번호는 {1}입니다".format(url, password))