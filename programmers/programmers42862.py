def solution(n, lost, reserve):
    answer = 0
    students = [1 for _ in range(n)]
    
    for num in lost:
        students[num-1] -= 1
    
    for num in reserve:
        students[num-1] += 1
        
    if students[0] == 0 and students[1] == 2:
        students[1] -= 1
        students[0] += 1
        
    for i in range(1, n):
        if students[i-1] == 0 and students[i] == 2:
            students[i-1] += 1
            students[i] -= 1
            
    if students[n-1] == 0 and students[n-2] == 2:
        students[n-2] -= 1
        students[n-1] += 1
        
    for i in range(n):
        if students[i] > 0:
            answer += 1
            
    return answer