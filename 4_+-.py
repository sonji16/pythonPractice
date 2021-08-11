n = input()
my_list = input().split(" ")
int_list = []
num_list = []
add_list = []

for i in my_list:
   int_list.append(int(i))


'''
for j in range(n):
    int_list[j]
    
for j in range(n - 1):
    int_list[j] + int_list[j + 1]

for j in range(n - 2):
    int_list[j] + int_list[j + 1] + int_list[j + 2]

for j in range(n - 3):
    int_list[j] + int_list[j + 1] + int_list[j + 2] + int_list[j + 3]

for j in range(n - 4):
    int_list[j] + int_list[j + 1] + int_list[j + 2] + int_list[j + 3] + int_list[j + 4]
for j in range(n - 6):
    int_list[j] + int_list[j + 1] + int_list[j + 2] + int_list[j + 3] + int_list[j + 4] + int_list[j + 5] + int_list[j + 6]
'''

for m in range(n):
    for j in range(n - m):
        for k in range(m + 1):
            l = j + k
            add_num = int_list[l]
            add_list.append(add_num)
        num_list.append(sum(add_list))
        add_list = []

print(max(num_list))