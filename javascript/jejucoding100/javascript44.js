function sumDigit(num) {
    var result = 0;
    while (num) {
        result += num % 10;
        num = parseInt(num / 10, 10);
    }
    return result;
}

var num = 18234;
console.log(sumDigit(num));

num = 3849;
console.log(sumDigit(num));