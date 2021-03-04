numbers = list(map(int, input().split(', ')))
odds = [odd for odd in numbers if odd % 2]

for i in range(len(odds)-1):
    print(odds[i], end=', ')
print(odds[-1])