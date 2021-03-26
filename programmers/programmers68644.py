def solution(numbers):
    answer = []
    check = [0 for _ in range(201)]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_number = numbers[i] + numbers[j]
            if not check[sum_number]:
                check[sum_number] = 1
    
    for i in range(201):
        if check[i]:
            answer.append(i)
            
    return answer