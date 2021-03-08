firstStr = input()
secondStr = input()

R, C = len(firstStr), len(secondStr)
common = [['' for _ in range(C+1)] for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        common[i][j] = common[i][j-1]
        if len(common[i][j]) < len(common[i-1][j]):
            common[i][j] = common[i-1][j]
        if firstStr[i-1] == secondStr[j-1]:
            if len(common[i][j]) < len(common[i-1][j-1]) + 1:
                common[i][j] = common[i-1][j-1] + firstStr[i-1]

print(common[-1][-1])