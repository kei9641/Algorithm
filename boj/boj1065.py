N = int(input())
if N < 100:
    result = N
else:
    result = 99
    hundred = N // 100
    result += (hundred - 1) * 5

    for d in range(-4, 5):
        digit = hundred
        turn = 2
        num = digit
        while turn:
            num += d
            if 0 <= num < 10:
                digit = digit * 10 + num
            else: 
                break
            turn -= 1

        if 100 < digit <= N:
            result += 1

print(result)