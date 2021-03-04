init_list = [12, 24, 35, 70, 88, 120, 155]
result = [init_list[idx] for idx in range(len(init_list)) if idx % 2]
print(result)