function digitSum(n) {
    var sum = 0;
    while (n) {
        sum += n % 10;
        n = parseInt(n / 10, 10);
    }
    return sum;
}

var result = 0;
for (var n=10; n<=15; n++) {
    result += digitSum(n)
}
console.log(result);