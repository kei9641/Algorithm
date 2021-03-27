def solution(w,h):
    answer = 0
    # 12번 시간초과 해결    
    if w == h:
        return w ** 2 - w
    # 11번 시간초과 해결
    elif w == 1 or h == 1:
        return 0
    else:
        a, b = -(h/w), h
        for i in range(1, w+1):
            answer += int(a*i+b)
        return answer * 2
    
# 시간초과를 고려하여 예외처리 필수!!