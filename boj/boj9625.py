K = int(input())

count = [0, 1]
for n in range(2, K + 1):
    count.append(count[n-1] + count[n-2])

print(count[-2], count[-1])