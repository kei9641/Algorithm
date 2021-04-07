var str = 'hi';

var fillStr = str.padStart(25 + parseInt(str.length / 2, 10), '=').padEnd(50, '=');
console.log(fillStr);