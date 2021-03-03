# 입력
T = int(input())
for testcase in range(T):
    string = input()
    
    # 처음과 끝 값 확인
    if string[-1] == "(" or string[0] == ")":
        print("NO")
        continue
    
    # 선언
    VPS = ["("]
    
    # 괄호 쌍 검사
    for i in range(1, len(string)):
        # "(" 는 push
        if string[i] == "(":
            VPS.append(string[i])
        # ")" 는 괄호 쌍이 있으면 pop 
        elif VPS:
            VPS.pop()
        # pop할 수 없는 경우
        else:
            print("NO")
            break
    # 검사 끝 & 출력
    else:
        # 괄호 쌍을 다 찾지 못한 경우
        if VPS:
            print("NO")
        # 괄호 쌍을 다 찾은 경우
        else:
            print("YES")
            