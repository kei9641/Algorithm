L = int(input())
for _ in range(L):
    password = input()
    before, after = [], []
    
    for word in password:
        if word == '<':
            if before:
                after.append(before.pop())
        elif word == '>':
            if after:
                before.append(after.pop())
        elif word == '-':
            if before:
                before.pop()
        else:
            before.append(word)

    print(''.join(before + list(reversed(after))))