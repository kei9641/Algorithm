def fibonacci(N):
    global fibo_0, fibo_1
    a, b = 1, 0

    for _ in range(N):
        a, b = b, a + b
    fibo_0, fibo_1 = a, b
    return fibo_1

T = int(input())
for tc in range(T):
    N = int(input())
    fibonacci(N)
    print('{} {}'.format(fibo_0, fibo_1))