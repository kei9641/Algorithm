from collections import defaultdict

delete = []
N = int(input())
relation = list(map(int, input().split()))
tree = defaultdict(list)
d = int(input())

for node, root in enumerate(relation):
    if node == d or root == d:
        continue

    if root == -1:
        delete.append(node)
    else:
        tree[root].append(node)

leaf = 0
while delete:
    node = delete.pop()
    if not node in tree:
        leaf += 1
    else:
        delete += tree[node]
print(leaf)