# 입력
S = input()

# 선언
alphabet = [-1] * 26

# 알파벳 위치 구하기
for i in range(len(S)):
    word = ord(S[i]) - ord('a')
    if alphabet[word] == -1:
        alphabet[word] = i

# 출력
print(*alphabet)