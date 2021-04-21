from collections import defaultdict, deque

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a, b, v = map(int, input().split())
    tree[a].append((b, v))
    tree[b].append((a, v))

def bfs(node_num):
    deq = deque()
    deq.append(node_num)
    visited = [-1 for _ in range(n+1)]
    visited[node_num] = 0

    while deq:
        current_node = deq.popleft()
        for node, value in tree[current_node]:
            if visited[node] == -1:
                visited[node] = visited[current_node] + value
                deq.append(node)

    max_value = max(visited)
    return visited.index(max_value), max_value

start_node, value = bfs(1)
end_node, diameter = bfs(start_node)
print(diameter)