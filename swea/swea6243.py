words = input().split()
result = list(set(words))
result.sort()
for i in range(len(result)-1):
    print(result[i], end=',')
print(result[-1])