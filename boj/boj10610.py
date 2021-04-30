N = list(input())
digit_sum = 0
zero = False

for num in N:
    digit_sum += int(num)
    if num == '0':
        zero = True

if zero and (digit_sum % 3 == 0):
    N.sort(reverse=True)
    print(''.join(N))
else:
    print(-1)
    