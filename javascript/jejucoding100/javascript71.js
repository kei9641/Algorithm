var graph = {
    'E': ['D', 'A'],
    'F': ['D'],
    'A': ['E', 'C', 'B'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E','F']
};

var visited = [];
function dfs(start) {
    visited.push(start);
    for (var node of graph[start]) {
        if (!visited.includes(node)) {
            dfs(node);
        }
    }
}
dfs('E');
console.log(visited.join(' '));