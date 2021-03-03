# 입력
N = int(input())
haveNum = list(map(int, input().split()))
M = int(input())
showNum = list(map(int, input().split()))

# 선언
cards = {}
cardCnt = [0 for _ in range(M)]

# 가진 카드 수
for num in haveNum:
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

# 주어진 카드 수
for i in range(M):
    if showNum[i] in cards:
        cardCnt[i] = cards[showNum[i]]

# 출력
print(*cardCnt)