row = list()
column = list()

numbers = input()
number = list(map(int, numbers.split(', ')))

for i in range(number[0]):
    for j in range(number[1]):
        column.append(i*j)
    row.append(column)
    column = list()
print(row)