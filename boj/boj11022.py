T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(test_case+1, A, B, A+B))