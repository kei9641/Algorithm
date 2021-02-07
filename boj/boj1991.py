from collections import defaultdict

tree = defaultdict(list)
N = int(input())
for _ in range(N):
    node, left, right = input().split()
    tree[node].extend([left, right])

def first(n):
    result = n
    if tree[n][0] != '.':
        result += first(tree[n][0])
    if tree[n][1] != '.':
        result += first(tree[n][1])
    return result

def center(n):
    result = ''
    if tree[n][0] != '.':
        result += center(tree[n][0])
    result += n
    if tree[n][1] != '.':
        result += center(tree[n][1])
    return result

def last(n):
    result = ''
    if tree[n][0] != '.':
        result += last(tree[n][0])
    if tree[n][1] != '.':
        result += last(tree[n][1])
    result += n
    return result

print(first('A'))
print(center('A'))
print(last('A'))
