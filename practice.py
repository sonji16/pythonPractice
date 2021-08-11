from random import randint


data = []
for i in range(50):
    a = randint(0, 1)
    data.append(a)

result = data.count(0)
print(result)