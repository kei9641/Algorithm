stack = []

S = input()
i = len(S) - 1
length = 0
while i >= 0:
    if S[i] == ')':
        stack.append(')')
        i -= 1
    elif S[i] == '(':
        while str(stack[-1]).isdigit():
            length += int(stack.pop())
        stack.pop()
        stack.append(int(S[i-1]) * length)
        length = 0
        i -= 2
    else:
        while i >= 0 and S[i].isdigit():
            length += 1
            i -= 1
        stack.append(length)
        length = 0

unzip = sum(stack)
print(unzip)