var graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
};

var visited = [];
var queue = [['A', 0]];

function bfs(end) {
    while (queue.length) {
        var [node, r] = queue.shift();
        visited.push(node);
        if (node === end) {
            return r;
        }
        for (var n of graph[node]) {
            if (!visited.includes(n)) {
                queue.push([n, r + 1]);
            }
        }
    }
}

console.log(bfs('F'));
