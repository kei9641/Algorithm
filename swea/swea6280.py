number = int(input())
divide_num = list()

for i in range(1, number+1):
    if number % i == 0:
        divide_num.append(i)

print(divide_num)