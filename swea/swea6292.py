input_str = input().split(', ')
list_num = list()

for i in range(len(input_str)):
    list_num.append(int(input_str[i]))
tuple_num = tuple(list_num)
print(list_num)
print(tuple_num)