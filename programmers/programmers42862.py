def solution(n, lost, reserve):
    answer = 0
    
    students = [1 for _ in range(n)]
    for num in reserve:
        students[num-1] += 1
    for num in lost:
        students[num-1] -= 1
        
    for i in range(n):
        if students[i] == 2:
            if i > 0 and students[i-1] == 0:
                students[i] -= 1
                students[i-1] += 1
            elif i+1 < n and students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1
    
    for i in range(n):
        if students[i] > 0:
            answer += 1
            
    return answer