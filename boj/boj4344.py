C = int(input())
for tc in range(C):
    scores = list(map(int, input().split()))
    average = (sum(scores) - scores[0]) / scores[0]
    
    highStudent = 0
    for i in range(1, scores[0] + 1):
        if scores[i] > average:
            highStudent += 1
    
    print("{:.3f}%".format(highStudent / scores[0] * 100))