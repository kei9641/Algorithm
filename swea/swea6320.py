p1 = input()
p2 = input()
g1 = input()
g2 = input()

if(g1 == '가위'):
    if(g2 == '가위'):
        print("비겼습니다!")
    elif(g2 == '바위'):
        print("%s가 이겼습니다!" %g2)
    elif(g2 == '보'):
        print("%s가 이겼습니다!" %g1)
elif(g1 == '바위'):
    if(g2 == '가위'):
        print("%s가 이겼습니다!" %g1)
    elif(g2 == '바위'):
        print("비겼습니다!")
    elif(g2 == '보'):
        print("%s가 이겼습니다!" %g2)
elif(g1 == '보'):
    if(g2 == '가위'):
        print("%s가 이겼습니다!" %g2)
    elif(g2 == '바위'):
        print("%s가 이겼습니다!" %g1)
    elif(g2 == '보'):
        print("비겼습니다!")