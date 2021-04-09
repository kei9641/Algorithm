var a = [[1, 2], [2, 4]];
var b = [[1, 0], [0, 3]];
var result = [];

if (a[0].length !== b.length) {
    result = -1;
} else {
    for (var i = 0; i < a.length; i++) {
        var row = [];
        for (var j = 0; j < a.length; j++) {
            var sum = 0;
            for (var k = 0; k < a.length; k++) {
                sum += a[i][k] * b[k][j];
            }
            row.push(sum);
        }
        result.push(row);
    }
}
console.log(result);