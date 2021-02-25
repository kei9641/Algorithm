# 입력
M, N = map(int, input().split())
board = [list(input()) for _ in range(M)]

# 선언
whiteChess = [list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW')]
blackChess = [list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB'), list('BWBWBWBW'), list('WBWBWBWB')]
minPnt = 2500

# 8x8로 자르기
for startX in range(M-7):
    for startY in range(N-7):
        whitePaint = 0
        blackPaint = 0
        # 체스판과 보드를 비교하여 다시 칠할 부분을 세기
        for i in range(8):
            for j in range(8):
                if whiteChess[i][j] != board[startX+i][startY+j]:
                    whitePaint += 1
                if blackChess[i][j] != board[startX+i][startY+j]:
                    blackPaint += 1
        # 가장 적게 칠하는 경우
        if minPnt > whitePaint:
            minPnt = whitePaint
        if minPnt > blackPaint:
            minPnt = blackPaint

# 출력
print(minPnt)
