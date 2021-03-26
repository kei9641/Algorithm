from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    total_weight = 0
    i = 0
    
    while 1:
        answer += 1
        for j in range(len(bridge)):
            bridge[j][0] += 1
        if bridge and bridge[0][0] > bridge_length:
            total_weight -= bridge[0][1]
            bridge.popleft()
        if i >= len(truck_weights):
            if not bridge:
                break
        elif total_weight + truck_weights[i] <= weight:
            bridge.append([1, truck_weights[i]])
            total_weight += truck_weights[i]
            i += 1
            
    return answer

l, w = map(int, input().split())
weights = list(map(int, input().split()))
print(solution(l, w, weights))
