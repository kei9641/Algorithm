def solution(numbers, hand):
    answer = ''
    numPos = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    Xl, Yl, Xr, Yr = 3, 0, 3, 2
    for number in numbers:
        Xt, Yt = numPos[number]
        if Yt == 0:
            Xl, Yl = Xt, Yt
            answer += "L"
            continue
        elif Yt == 2:
            Xr, Yr = Xt, Yt
            answer += "R"
            continue
        disL = abs(Xl - Xt) + abs(Yl - Yt)
        disR = abs(Xr - Xt) + abs(Yr - Yt)
        if disL < disR:
            Xl, Yl = Xt, Yt
            answer += "L"
        elif disL > disR:
            Xr, Yr = Xt, Yt
            answer += "R"
        elif hand == "left":
            Xl, Yl = Xt, Yt
            answer += "L"
        elif hand == "right":
            Xr, Yr = Xt, Yt
            answer += "R"
    return answer