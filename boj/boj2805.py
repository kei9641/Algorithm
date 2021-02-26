# 입력
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 선언
minH, maxH = 1, max(trees)

# 나무 자르기(binary search)
while minH <= maxH:
    midH = (minH + maxH) // 2
    cutTree = 0
    for tree in trees:
        if tree > midH:
            cutTree += tree - midH
    if cutTree >= M:
        minH = midH + 1
    else:
        maxH = midH - 1

# 출력
print(maxH)