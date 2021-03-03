# 입력
A, B = map(int, input().split())

multiAB = A * B

# 최대공약수(유클리드 호제법)
while(B):
    A, B = B, A % B
GCD = A

# 최소공배수
LCM = multiAB // GCD

# 출력
print(GCD)
print(LCM)