# 입력
L = int(input())
S = list(input())

# 선언
r = 31
M = 1234567891
hashing = 0

# 해쉬 변환
for i in range(len(S)):
    a = ord(S[i]) - ord('a') + 1
    hashing += a * (r ** i)
hashing %= M

# 출력
print(hashing)