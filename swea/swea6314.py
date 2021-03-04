'''
# 2. lambda 입력값: 명령문 : 입력값을 명령문에 대입하여 나온 값을 반환
a = lambda x: x+5
b = a(7)
print(b)
'''
a = range(1, 11)
def even(x):
    b = lambda x: (x % 2 == 0)
    return b(x)
result = list(filter(even, range(1, 11)))
print(result)