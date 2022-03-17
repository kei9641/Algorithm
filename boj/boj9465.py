from random import randrange


T = int(input())
for tc in range(T):
    n = int(input())

    board = []
    for _ in range(2):
        board.append([0] + list(map(int, input().split())))

    for i in range(2, n + 1):
        board[0][i] += max(board[1][i - 1], board[1][i - 2])
        board[1][i] += max(board[0][i - 1], board[0][i - 2])

    print(max(board[0][-1], board[1][-1]))