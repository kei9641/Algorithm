# 테스트케이스 수
T = int(input())

for tc in range(T):
    # 입력
    R, S = input().split()

    # 선언
    reString = ''
    string = list(S)

    # 문자 반복
    for word in string:
        reString += word * int(R)
    # 출력
    print(reString)
