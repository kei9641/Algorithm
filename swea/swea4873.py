T = int(input())
for tc in range(T):
    s = input()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print('#{} {}'.format(tc+1, len(stack)))