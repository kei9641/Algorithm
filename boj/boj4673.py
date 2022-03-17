nums = list(1 for _ in range(10001))

for i in range(1, 10001):
    for j in str(i):
        i += int(j)

    if i < 10001:
        nums[i] = 0

for i in range(1, 10001):
    if nums[i]:
        print(i)