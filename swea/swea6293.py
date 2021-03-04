Pi = 3.141592
input_str = input().split(', ')
circle = 0

for i in range(len(input_str)-1):
    input_num = int(input_str[i])
    circle = 2 * Pi * input_num
    print('{:.2f}'.format(circle), end=', ')
input_num = int(input_str[-1])
circle = 2 * Pi * input_num
print('{:.2f}'.format(circle))