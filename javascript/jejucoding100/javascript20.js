var input = '10 2'.split(' ');

var a = parseInt(input[0], 10);
var b = parseInt(input[1], 10);

var div = Math.floor(a / b);
var mod = a % b;

console.log(div, mod);