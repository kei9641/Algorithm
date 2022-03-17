X, Y = input().split()

def REV(words):
    return int(words[::-1])

print(REV(str(REV(X) + REV(Y))))