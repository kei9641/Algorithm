var keys = 'Yujin Hyewon'.split(' ');
var values = '70 100'.split(' ');

var math = {};
for (var i=0; i<keys.length; i++) {
    math[keys[i]] = parseInt(values[i], 10);
}

console.log(math);