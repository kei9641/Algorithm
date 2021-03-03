import sys
 
# 테스트케이스는 입력하는 줄의 수
for line in sys.stdin:
    # 입력
    A, B = map(int, line.split())
    # 출력
    print(A + B)