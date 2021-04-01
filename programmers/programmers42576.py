def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    else:
        answer = participant[-1]
        
    return answer