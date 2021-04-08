var a = [1, 2, 3, 4];
var b = ['a', 'b', 'c', 'd'];

for (var [key, value] of a.entries()) {
    if (key % 2 == 0) {
        console.log([value, b[key]]);
    } else {
        console.log([b[key], value]);
    }
}