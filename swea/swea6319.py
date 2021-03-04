a = input()
b = list(a)
c = list()

def rev():
    for i in reversed(range(len(b))):
        c.append(b[i])
    return c
        
x = rev()
for i in range(len(b)):
    print(c[i], end="")
if(x == c):
    print("\n입력하신 단어는 회문(Palindrome)입니다.")