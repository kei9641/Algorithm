winner, maxScore = 0, 0

for n in range(1, 6):
    scores = list(map(int, input().split()))
    if (maxScore < sum(scores)):
        maxScore = sum(scores)
        winner = n

print(winner, maxScore)
