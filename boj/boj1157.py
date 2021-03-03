# 입력
string = input().upper()
# 선언
alphabet = {}
maxAlpha = ''
maxCnt = 0

for word in string:
    # 알파벳 수 세기
    if word in alphabet:
        alphabet[word] += 1
    else:
        alphabet[word] = 1
    # 가장 많은 수의 알파벳 찾기
    if alphabet[word] > maxCnt:
        maxAlpha = word
        maxCnt = alphabet[word]
    elif alphabet[word] == maxCnt:
        maxAlpha = '?'

# 출력
print(maxAlpha)