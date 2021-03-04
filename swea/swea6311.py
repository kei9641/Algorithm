'''
# 1. map(함수, 리스트) : 리스트 값을 차례대로 하나씩 함수에 대입
a = [1, 2, 3, 4, 5, 6]
def make_double(x):
	return x * 2

result = list(map(make_double, a))
print(result)

# 2. lambda 입력값: 명령문 : 입력값을 명령문에 대입하여 나온 값을 반환
a = lambda x: x+5
b = a(7)
print(b)
'''
a = list('ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC')
b = list(map(lambda x : ord('E') - ord(x), a))
print(sum(b))
