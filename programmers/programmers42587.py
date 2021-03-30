from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        work = queue.popleft()
        for j in range(len(queue)):
            if queue[j][0] > work[0]:
                queue.append(work)
                break
        else:
            answer += 1
            if work[1] == location:
                break
                
    return answer