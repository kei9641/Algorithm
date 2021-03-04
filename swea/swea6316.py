num = range(1, 11)
even = list(filter(lambda x: x % 2 == 0, num))
squr = list(map(lambda x: x ** 2, even))
print(squr)