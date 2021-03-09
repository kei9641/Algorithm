def solution(dartResult):
    answer = 0
    bonus = ['S', 'D', 'T']
    scores = []
    point = ''
    idx = -1
    for i in range(len(dartResult)):
        if dartResult[i] in bonus:
            scores.append(int(point))
            idx += 1
            if dartResult[i] == 'D':
                scores[idx] = scores[idx]**2
            elif dartResult[i] == 'T':
                scores[idx] = scores[idx]**3
            point = ''
        elif dartResult[i] == '*':
            scores[idx] *= 2
            if idx:
                scores[idx-1] *= 2
        elif dartResult[i] == '#':
            scores[idx] *= -1
        else:
            point += dartResult[i]
    for j in range(len(scores)):
        answer += scores[j]
    return answer