num = [3, 5, 4, 1, 8, 10, 2]
mx = 0
for i in range(len(num) - 1):
    if num[i] >= num[i + 1]:
        mx = num[i]
    else:
        mx = num[i + 1]
print('max{} => {}'.format(tuple(num), mx))