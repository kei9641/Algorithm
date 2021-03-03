while 1:
    # 입력
    a, b, c = map(int, input().split())
    
    # 종료
    if (a, b, c) == (0, 0, 0):
        break

    # 제곱
    a *= a
    b *= b
    c *= c

    # 출력
    if a == b + c or b == a + c or c == a + b:
        print("right")
    else:
        print("wrong")
