while 1:
    # 선언
    balance = []

    # 입력
    S = input()

    # 종료 조건
    if S == ".":
        break

    # 균형잡힌 문자열인지 판단
    for word in S:
        if word == '(' or word == '[':
            balance.append(word)
        elif word == ')':
            if balance:
                if balance[-1] == '(':
                    balance.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        elif word == ']':
            if balance:
                if balance[-1] == '[':
                    balance.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break
    else:
        if balance:
            print("no")
        else:
            print("yes")
