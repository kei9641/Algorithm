board = dict()

bingo, turn = 0, 0
boardRow = [0 for _ in range(5)]
boardCol = [0 for _ in range(5)]
diagLeft, diagRight = 0, 0

for r in range(5):
    nums = list(map(int, input().split()))
    for c in range(len(nums)):
        board[nums[c]] = [r, c]

for i in range(5):
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        x, y = board[nums[j]]

        boardRow[x] += 1
        if boardRow[x] == 5:
            bingo += 1

        boardCol[y] += 1
        if boardCol[y] == 5:
            bingo += 1

        if x == y:
            diagLeft += 1
            if diagLeft == 5:
                bingo += 1

        if x + y == 4:
            diagRight += 1
            if diagRight == 5:
                bingo += 1

        if bingo >= 3:
            if turn == 0:
                turn = i * 5 + j + 1
            break
            
print(turn)