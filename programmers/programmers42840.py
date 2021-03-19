firstAnswer = [1, 2, 3, 4, 5]
secondAnswer = [2, 1, 2, 3, 2, 4, 2, 5]
thirdAnswer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    
    scores = [0 for _ in range(3)]
    for i in range(len(answers)):
        num = answers[i]
        if num == firstAnswer[i % 5]:
            scores[0] += 1
        if num == secondAnswer[i % 8]:
            scores[1] += 1
        if num == thirdAnswer[i % 10]:
            scores[2] += 1
    
    max_score = 0
    for j in range(3):
        score = scores[j]
        if max_score < score:
            max_score = score
            answer = [j+1]
        elif max_score == score:
            answer.append(j+1)
            
    return answer