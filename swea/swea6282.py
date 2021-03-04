number_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
even_list = list()

for i in number_list:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)