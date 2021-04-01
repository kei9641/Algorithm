days = {
    1 : 31,
    2 : 29,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

def solution(a, b):
    answer = ''
    
    day = b - 1
    for m in range(1, a):
        day += days[m]
        
    answer = week[day % 7]
    
    return answer