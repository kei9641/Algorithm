max_weight = 0
rope = []
N = int(input())
for _ in range(N):
    weight = int(input())
    max_weight = max(max_weight, weight)
    rope.append(weight)

rope.sort(reverse=True)
for i in range(N):
    max_weight = max(max_weight, rope[i] * (i + 1))

print(max_weight)