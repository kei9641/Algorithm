var num = 16;

var digit = [];
while (num) {
    digit.push(num % 2);
    num = parseInt(num / 2, 10);
}

console.log(digit.reverse().join(''));