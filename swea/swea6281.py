number = int(input())

divide_num = [i for i in range(1, number+1) if (number % i == 0)]

print(divide_num)