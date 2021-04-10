var graph = {
    'E': ['D', 'A'],
    'F': ['D'],
    'A': ['E', 'C', 'B'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E','F']
};

var visited = [];
var queue = ['E'];
function bfs() {
    while (queue.length) {
        node = queue.shift();
        visited.push(node);
        for (var n of graph[node]) {
            if (!visited.includes(n)) {
                queue.push(n);
            }
        }
    }
}

bfs()
console.log(visited.join(' '));