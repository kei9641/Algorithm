memo = dict()
N, M = map(int, input().split())
for _ in range(N):
    url, pw = input().split()
    memo[url] = pw

for _ in range(M):
    find = input()
    print(memo[find])