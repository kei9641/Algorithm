def solution(n):
    answer = 0
    three = ''
    while n // 3:
        three += str(n % 3)
        n //= 3
    three += str(n)
    
    answer = int(three, 3)
    
    return answer