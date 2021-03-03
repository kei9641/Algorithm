# 입력
N, M = map(int, input().split())
card = list(map(int, input().split()))

# 선언
blackJack = 0

# 카드 뽑기
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cardSum = card[i] + card[j] + card[k]
            # 블랙잭을 넘으면 다시 카드 뽑기
            if cardSum > M:
                continue
            elif blackJack < cardSum:
                blackJack = cardSum

# 출력
print(blackJack)
