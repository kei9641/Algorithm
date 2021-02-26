# 입력
N = int(input())
scores = list(map(int, input().split()))

# 선언
operation = 0

# 점수 조작
maxScr = max(scores)
for score in scores:
    operation += score/maxScr*100

# 출력
print(operation/len(scores))
