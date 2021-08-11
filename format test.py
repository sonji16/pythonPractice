# (문자) < (폭)  왼쪽정렬
result1 = "{0:<10}".format(5)
print(result1)
result2 = "{0:0<10}".format(5)
print(result2)
result3 = "{0:x<10}".format(5)
print(result3)

# (문자) > (폭)  오른쪽 정렬

result4 = "{0:>10}".format(5)
print(result4)
result5 = "{0:0>10}".format(5)
print(result5)
result6 = "{0:x>10}".format(5)
print(result6)

# (문자) ^ (폭)  가운데 정렬
result7 = "{0:^10}".format(5)
print(result7)
result8 = "{0:0^10}".format(5)
print(result8)
result8 = "{0:x ^10}".format(5)
print(result8)